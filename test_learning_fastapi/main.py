
import asyncio
import time


async def cook_order(table_number,cook_time):
    print("Waiter:Took order from the table {table_number}.sent to the kitchen.")
    await asyncio.sleep(cook_time)
    
    print("Kitchen:Food for table {table_number} is ready")
    

async def main():
    start_time=time.time()
    print("Restaurant is open.Waiter is ready to take order")
    
    await asyncio.gather(
        cook_order("A",13),
        cook_order("B",14),
        cook_order("C",15)
        )
    end_time=time.time()
    print(f"\nAll tables served in {end_time - start_time:.2f} seconds.")
if __name__ == "__main__":
    asyncio.run(main())
