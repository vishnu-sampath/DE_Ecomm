# High-Level Architecture (Local-Only)

CSV Files
   ↓
MySQL (Source Database)
   ↓
Apache Spark (Batch Processing)
   ↓
Hive Tables (Local / Docker)
   ↓
Apache Druid
   ↓
Power BI Desktop
