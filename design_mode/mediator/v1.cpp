#define _CRTDBG_MAP_ALLOC
#include <crtdbg.h>

#include <iostream>
#include <string>
#include <sstream>
#include <vector>

class BoxSelectorMediator;

class Widget {
public:
    Widget(Widget* parent = nullptr): _parent(parent), _mediator(nullptr) {
        if (_parent) _parent->setChildren(this);
    };
    virtual ~Widget() {
        for (Widget* child : _children) {
            delete child;
        }
    };
    virtual void draw() {};
    virtual void draw(std::stringstream&) {};
    virtual void change();
    void setMediator(BoxSelectorMediator* mediator) {_mediator = mediator;};
    void show(std::stringstream* canvas = nullptr) {
        bool free_sign = false;
        if (!canvas) {
            canvas = new std::stringstream();
            free_sign = true;
        }
        draw(*canvas);
        for (Widget* child : _children) {
            child->draw(*canvas);
        }
        std::cout << (*canvas).str();
        if (free_sign) delete canvas;
    };
    virtual void setText(const std::string& text) {_text = text;};
    virtual std::string text() {return _text;};
    void setChildren(Widget* children = nullptr) {
        if (!children) return;
        _children.push_back(children);
    };

private:
    BoxSelectorMediator* _mediator;

    Widget* _parent;
    std::vector<Widget*> _children;

    std::string _text;
};

class ListBox : public Widget {
public:
    ListBox(Widget* parent = nullptr): Widget(parent), _current_idx(0) {};
    void draw(std::stringstream&) override;
    void addItem(const std::string& item) {_items.push_back(item);};
    void addItems(const std::vector<std::string>& items) {_items.insert(_items.end(), items.begin(), items.end());};
    void clear() {_items.clear();};
    std::string currentText() {return _items.at(_current_idx);};
    void setCurrentIdx(int idx) {_current_idx = idx;};
private:
    std::vector<std::string> _items;
    int _current_idx;
};

void ListBox::draw(std::stringstream& canvas) {
    canvas << "----- ListBox ----\n";
    for (const auto& item : _items) {
        canvas << "-----" << item  << "-----\n";
    }
    canvas << "----- End ----\n";
}

class Button : public Widget {
public:
    Button(Widget* parent = nullptr): Widget(parent) {};
    void draw(std::stringstream&) override;
    void click() {change();};
private:
};

void Button::draw(std::stringstream& canvas) {
    canvas << "| Button: " << text() << " |\n";
}

class TextBox : public Widget {
public:
    TextBox(Widget* parent = nullptr): Widget(parent) {};
    void draw(std::stringstream&) override;
};

void TextBox::draw(std::stringstream& canvas) {
    canvas << "| TextBox: " << text() << " |\n";
}

class BoxSelectorMediator {
public:
    BoxSelectorMediator(): _lb(nullptr), _b(nullptr), _tb(nullptr) {}
    virtual ~BoxSelectorMediator() = default;
    virtual void widgetStateChange(Widget* widget);
    virtual void showDialog();
    void createWidgets();
    void userInput(int way);
private:
    std::stringstream _canvas;
    Widget _base_widget;
    ListBox* _lb;
    Button* _b;
    TextBox* _tb;
};

void BoxSelectorMediator::createWidgets() {
    _lb = new ListBox(&_base_widget);
    _lb->addItem("Item 1");
    _lb->addItem("Item 2");
    _lb->addItem("Item 3");
    _b = new Button(&_base_widget);
    _b->setText("bt1");
    _tb = new TextBox(&_base_widget);
    _tb->setText("tb1");
    _base_widget.setMediator(this);
    _lb->setMediator(this);
    _b->setMediator(this);
    _tb->setMediator(this);
}

void BoxSelectorMediator::widgetStateChange(Widget* widget) {
    if (widget == _b) {
        _tb->setText(_lb->currentText());
    }
}

void BoxSelectorMediator::showDialog() {
    _canvas.clear();
    _canvas.str("");
    _base_widget.show(&_canvas);
}

void BoxSelectorMediator::userInput(int way) {
    switch (way) {
        case 0:
            _b->click();
            break;
        case 1:
            _lb->setCurrentIdx(0);
            break;
        case 2:
            _lb->setCurrentIdx(1);
            break;
        case 3:
            _lb->setCurrentIdx(2);
            break;
    }
}

void Widget::change() {
    if (_mediator) _mediator->widgetStateChange(this);
}

int main(int argc, char **argv) {
    _CrtSetDbgFlag(_CRTDBG_ALLOC_MEM_DF | _CRTDBG_LEAK_CHECK_DF);
    _CrtSetReportMode(_CRT_WARN, _CRTDBG_MODE_FILE);
    _CrtSetReportFile(_CRT_WARN, _CRTDBG_FILE_STDOUT);
    
    BoxSelectorMediator mediator;
    mediator.createWidgets();
    mediator.showDialog();

    std::cout << "####################\n";
    mediator.userInput(3);
    mediator.userInput(0);
    mediator.showDialog();
    return 0;
}
