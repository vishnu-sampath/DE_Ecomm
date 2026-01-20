# inventory

## Description
Stores inventory snapshot data for products in warehouses.

Each row represents the available stock of a product at a warehouse on a specific date.

## Grain
One row per product per warehouse per snapshot date.

## Business Use Cases
- Stock level monitoring
- Inventory planning
- Supply chain analysis

## Columns
- inventory_id: Unique identifier for inventory record
- product_id: Identifier of the product
- warehouse_id: Identifier of the warehouse
- quantity_available: Units available in stock
- snapshot_date: Date of inventory snapshot

## Notes
- Inventory is captured as daily snapshots, not real-time data
