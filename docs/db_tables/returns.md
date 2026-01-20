# returns

## Description
Stores returned products related to previous sales.

Each row represents a returned product from a sale.

## Grain
One row per product per return.

## Business Use Cases
- Return rate analysis
- Refund calculations
- Product quality tracking

## Columns
- return_id: Unique identifier for the return
- sale_id: Identifier of the original sale
- product_id: Identifier of the returned product
- return_date: Date when the return occurred
- quantity_returned: Number of units returned
- unit_price: Price per unit at the time of sale
