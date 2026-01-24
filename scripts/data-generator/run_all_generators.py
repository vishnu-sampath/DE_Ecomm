from generate_products import main as generate_products
from generate_suppliers import main as generate_suppliers
from generate_stores import main as generate_stores
from generate_warehouses import main as generate_warehouses
from generate_customers import main as generate_customers
from generate_sales import main as generate_sales
from generate_inventory import main as generate_inventory
from generate_returns import main as generate_returns
from check_table_sizes import main as check_table_sizes

GENERATORS = [
    generate_products,
    generate_suppliers,
    generate_stores,
    generate_warehouses,
    generate_customers,
    generate_sales,
    generate_inventory,
    generate_returns
]

if __name__ == "__main__":
    try:
        for generator in GENERATORS:
            generator()
        print("\nAll scripts completed successfully\n")
        check_table_sizes()
    except Exception as e:
        print("Error:", e)
