import asyncio
import atexit
import discord
import random

from data import ensure_user_balance, load_balances, load_inventories, save_balances, save_inventories
from utils import has_prefix
from super_secret_token import CHECKOUT_TOKEN as TOKEN

from items import ITEMS

class SlefCheckoutBot:
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        self.client = discord.Client(intents=intents)
        self.baskets = {}
        self.inventories = load_inventories()
        self.items = ITEMS
        self.balances = load_balances()

        self.client.event(self.on_ready)
        self.client.event(self.on_message)
        self.client.event(self.on_disconnect)

        atexit.register(lambda: asyncio.run(self.on_disconnect()))

    async def on_ready(self):
        print("uhhhh hi i guess")
    
    async def on_disconnect(self):
        save_inventories(self.inventories)
        print("ok bye")

    async def on_message(self, message: discord.Message):
        if message.author == self.client.user:
            return

        user_id = str(message.author.id)
        self.balances = ensure_user_balance(user_id)

        if user_id not in self.baskets:
            self.baskets[user_id] = {}
        basket = self.baskets[user_id]
        inventory = self.inventories.get(user_id, {})

        if has_prefix(message, "$add"):
            await self.add_item(message, basket)
        elif has_prefix(message, "$basket"):
            await self.show_basket(message, basket)
        elif has_prefix(message, "$inventory") or has_prefix(message, "$inv"):
            await self.show_inventory(message, inventory)
        elif has_prefix(message, "$checkout"):
            await self.checkout(message, user_id, basket, inventory)
        elif has_prefix(message, "$items") or has_prefix(message, "$list"):
            await self.list_items(message)
        elif has_prefix(message, "$clear") or has_prefix(message, "$empty") or has_prefix(message, "$cls"):
            await self.clear_basket(message, user_id)
        elif has_prefix(message, "$remove"):
            await self.remove_item(message, basket)
        elif has_prefix(message, "$steal"):
            await self.steal_item(message, user_id, inventory)
        elif has_prefix(message, "$checkout_help") or has_prefix(message, "$chelp"):
            await self.show_help(message)





    async def add_item(self, message, basket):
        """add an item to the basket. usage: `$add <item> [<amount>]`"""
        try:
            command_and_args = message.content.split(" ", 1)[1]
            *item_parts, possible_amount = command_and_args.rsplit(" ", 1)

            if possible_amount.replace('.', '', 1).isdigit():
                amount = float(possible_amount)
                item_name = " ".join(item_parts).strip().lower()
            else:
                amount = 1
                item_name = command_and_args.strip().lower()
        except (ValueError, IndexError):
            await message.channel.send("usage: `$add <item> [<amount>]`")
            return

        if amount <= 0:
            await message.channel.send("amount must be greater than 0")
            return

        if item_name in self.items:
            basket[item_name] = basket.get(item_name, 0) + amount
            await message.channel.send(f"added {amount} {item_name} to your basket")
        else:
            await message.channel.send("item not available")





    async def show_basket(self, message, basket):
        if not basket:
            await message.channel.send("your basket is empty.")
            return

        total = sum(self.items[item] * amount for item, amount in basket.items())
        basket_summary = "\n".join(f"{item}: {int(amount)}" for item, amount in basket.items())
        await message.channel.send(f"your basket:\n{basket_summary}\ntotal: {total} R$")

    async def show_inventory(self, message, inventory):
        if not inventory:
            await message.channel.send("your inventory is empty.")
            return

        inventory_summary = "\n".join(f"{item}: {int(amount)}" for item, amount in inventory.items())
        await message.channel.send(f"your inventory:\n{inventory_summary}")





    async def checkout(self, message, user_id, basket, inventory):
        """purchase items in the basket. usage: `$checkout`"""
        if not basket:
            await message.channel.send("your basket is empty, go buy something you fucko")
            return

        total = sum(self.items[item] * amount for item, amount in basket.items())
        try:
            if self.balances[user_id] >= total:
                self.balances[user_id] -= total
                save_balances(self.balances)
                self.baskets[user_id] = {}
                for item, amount in basket.items():
                    self.inventories[str(user_id)][item] = self.inventories.get(user_id, {}).get(item, 0) + amount
                await message.channel.send(f"purchased items for {total} R$")
                await message.channel.send(f"new balance: {self.balances[user_id]} R$")
                await message.channel.send("thank you for shopping with us")
            else:
                await message.channel.send("insufficient funds (aka you're BROKE)")
        except TypeError:
            await message.channel.send("uh oh")




    async def list_items(self, message):
        """list available items ot purchase. usage: `$items`"""
        await message.channel.send("available items:\n" + "\n".join(f"- {item}: {price} R$" for item, price in self.items.items()))





    async def clear_basket(self, message, user_id):
        """empty the basket. usage: `$clear`"""
        self.baskets[user_id] = {}
        await message.channel.send("cleared basket")





    async def remove_item(self, message, basket):
        """remove an item from the basket. usage: `$remove <item> [<amount>]`"""
        try:
            command_and_args = message.content.split(" ", 1)[1]
            *item_parts, possible_amount = command_and_args.rsplit(" ", 1)

            if possible_amount.replace('.', '', 1).isdigit():
                amount = float(possible_amount)
                item_name = " ".join(item_parts).strip().lower()
            else:
                amount = 1
                item_name = command_and_args.strip().lower()
        except (ValueError, IndexError):
            await message.channel.send("usage: `$remove <item> [<amount>]`")
            return

        if amount <= 0:
            await message.channel.send("amount must be greater than 0")
            return

        if item_name in basket:
            if basket[item_name] <= amount:
                del basket[item_name]
            else:
                basket[item_name] -= amount
            await message.channel.send(f"removed {amount} {item_name} from your basket")
        else:
            await message.channel.send("item not in basket")





    async def steal_item(self, message, user_id, inventory):
        """attempt to steal an item from the store. usage: `$steal <item>`"""
        try:
            command_and_args = message.content.split(" ", 1)[1]
            item_name = command_and_args.strip().lower()
        except (ValueError, IndexError):
            await message.channel.send("usage: `$steal <item>`")
            return

        if item_name not in self.items:
            await message.channel.send("item not available")
            return

        steal_attempts = len(inventory)
        stolen_value = sum(self.items[item] for item in inventory)
        catch_chance = min(0.3 + 0.1 * steal_attempts + 0.1 * stolen_value / 100000, 0.9)

        if stolen_value > 1000000 or random.random() < catch_chance:
            self.balances[user_id] = 0
            save_balances(self.balances)
            self.inventories[user_id] = {}
            await message.channel.send("you got caught and lost all your money and inventory!")
        else:
            inventory[item_name] = inventory.get(item_name, 0) + 1
            self.inventories[user_id] = inventory
            await message.channel.send(f"successfully stole 1 {item_name} and added to your inventory")

    async def show_help(self, message):
        await message.channel.send(f"""commands (changed prefix from ! to $ to match my other bot):
        `items` or `list` - list available items
        `add <item> [<amount>]` - {self.add_item.__doc__}
        `remove <item> [<amount>]` - {self.remove_item.__doc__}
        `basket` - {self.show_basket.__doc__}
        `checkout` - {self.checkout.__doc__}
        `clear` - {self.clear_basket.__doc__}
        `inventory` or `inv` - {self.show_inventory.__doc__}
        `steal <item>` - {self.steal_item.__doc__}
        to use commands like $gift or $balance use retti's slave, the other bot. the balances are synced between these.
        """)

    def run(self):
        self.client.run(TOKEN)

if __name__ == "__main__":
    bot = SlefCheckoutBot()
    bot.run()
