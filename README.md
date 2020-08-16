# Book_Store_Flask

## 最後一次更新
加入user和purchase_history的model和schema，但table尚未建立。

要先建立關於user和purchase_history的api接口，然後在`main.py`中import：
```python
# 在這裡import
from api import book_store_api, book_api
```
```python
if __name__ == "__main__":
    migrate = Migrate(app, database.db)
    migrate.db.create_all() # <- 這裡會將用到db.Model的class建立table
    app.run()
```
