## Qt代理

代理是 Qt内部 `MVD`(Model-View-Delegate) 模式中的用户数据展示层
> QT使用 MVD 模式作为通用范式, 以解决: 大数据量下, 无法保留与展示相关的数据副本。这意味着在展示层(用户所看到的内容)，需要被数据层(实际内容)分隔开，即用户只关心显示部分的数据。

> 在自定义用户界面中使用模型和视图时, 代理在创建外观和行为方面扮演着重要角色。对模型中的每个元素都是通过代理来可视化，用户实际可见的是代理。

> 每个代理可以访问多个附加属性/数据, 对于模型相关数据存储一般使用 `setData/data` 管理, 如 `QAbstractItemModel` 派生类、`QListWidgetItem`、`QTableWidgetItem` 等


### 代理绘制中只绘制部分内容

QT的绘制系统是基于画家(Painter)的叠加原理工作的. 每次绘制都是在已有的内容上进行添加, 因此可以先调用基类的paint绘制元素, 之后在覆盖需要内容

**注意** 基类默认不绘制普通状态的背景, 只绘制选中状态, 可以使用 `QStyleOptionViewItem.backgroundBrush` 同时处理选中/非选中下的背景


### Cpp示例 

```cpp
class FullWidthDelegate : public QStyledItemDelegate {
public:
    explicit FullWidthDelegate(QObject *parent = nullptr) : QStyledItemDelegate(parent) {}
    
    QSize sizeHint(const QStyleOptionViewItem &option, const QModelIndex &index) const override {
        QSize size = QStyledItemDelegate::sizeHint(option, index);
        QListWidget *listWidget = qobject_cast<QListWidget*>(parent());
        if (listWidget)
        {
            QSize viewportSize = listWidget->viewport()->size();
            if (listWidget->flow() == QListWidget::TopToBottom) {
                size.setHeight((viewportSize.height()) / listWidget->count());
                size.setWidth(viewportSize.width());
            } else if (listWidget->flow() == QListWidget::LeftToRight) {
                size.setWidth((viewportSize.width()) / listWidget->count());
                size.setHeight(viewportSize.height());
            }
        }        
        return size;
    }
    
    void paint(QPainter *painter, const QStyleOptionViewItem &option, const QModelIndex &index) const override {
        QStyleOptionViewItem opt = option;
        initStyleOption(&opt, index);
        
        // 设置文本居中对齐
        opt.displayAlignment = Qt::AlignCenter;

        // 1. 绘制背景
        if (opt.state & QStyle::State_Selected) {
            painter->fillRect(opt.rect, opt.palette.highlight());
        } else {
            painter->fillRect(opt.rect, getBackgroundColor(index));
        }
        
        // 2. 绘制文本（居中对齐）
        painter->setFont(opt.font);
        QColor textColor = (opt.state & QStyle::State_Selected) 
                        ? opt.palette.highlightedText().color() 
                        : opt.palette.text().color();
        painter->setPen(textColor);
        
        painter->drawText(opt.rect, Qt::AlignCenter, opt.text);
        
        // 3. 绘制焦点框（如果需要）
        if (opt.state & QStyle::State_HasFocus) {
            QStyleOptionFocusRect focusOpt;
            focusOpt.rect = opt.rect.adjusted(1, 1, -1, -1);
            opt.widget->style()->drawPrimitive(QStyle::PE_FrameFocusRect, &focusOpt, painter);
        }
    }

    QColor FullWidthDelegate::getBackgroundColor(const QModelIndex &index) const
    {
        // 检查disable属性 (假设使用UserRole + 1存储disable属性)
        if (index.data(Qt::UserRole + 1).toBool()) {
            return Qt::gray; // 禁用状态为灰色
        }
        
        // 检查scan_text属性 (假设使用UserRole + 2存储scan_text)
        QString scanText = index.data(Qt::UserRole + 2).toString();
        if (!scanText.isEmpty()) {
            return QColor(144, 238, 144); // 浅绿色
        }
        
        // 默认背景色
        return QColor(240, 240, 240); // 浅灰色
    }
};
```

**注意事项** 
- `sizeHint` 计算 `item` 尺寸应使用视图 `viewport` 尺寸, 否则会出现显示不全/出现滑动条问题(因为一些线宽/边框等占用空间)