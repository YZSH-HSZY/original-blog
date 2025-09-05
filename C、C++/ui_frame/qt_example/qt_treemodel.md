## custom tree model 

`class CustomClass : public QAbstractItemModel`

重写方法:
- `QModelIndex parent(const QModelIndex &index) const override;`
- `QModelIndex index(int row, int column, const QModelIndex &parent = QModelIndex()) const override;`
- `QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override;`
- `int rowCount(const QModelIndex &parent = QModelIndex()) const override;`
- `int columnCount(const QModelIndex &parent = QModelIndex()) const override;`
- `QVariant headerData(int section, Qt::Orientation orientation, int role = Qt::DisplayRole) const override;`