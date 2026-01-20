# sales

## Description
Stores product-level sales transactions.

Each row represents a single product sold to a customer at a specific store and date.

## Grain
One row per product per sale.

## Business Use Cases
- Sales analysis
- Revenue reporting
- Trend analysis by product, store, or customer

## Columns
- sale_id: Unique identifier for the sale
- sale_date: Date when the sale occurred
- product_id: Identifier of the product sold
- customer_id: Identifier of the customer
- store_id: Identifier of the store where the sale occurred
- quantity: Number of units sold
- unit_price: Price per unit at the time of sale
