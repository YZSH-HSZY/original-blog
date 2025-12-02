## Qt中的Item

qt中item不像model一样具有统一的抽象基类, 只要各种独立的item类, 如:
- `QListWidgetItem`: 用于 `QListWidget`
- `QTableWidgetItem`: 用于 `QTableWidget`
- `QTreeWidgetItem`: 用于 `QTreeWidget`

> 这些 `*WidgetItem` 类是在 Qt 4 早期引入的, 当时 MVC 模式(Model/View)还没有完全整合
> 对于新项目, 推荐直接使用 `Model/View` 架构, 它提供了真正的统一抽象 `QAbstractItemModel` 和更好的灵活性