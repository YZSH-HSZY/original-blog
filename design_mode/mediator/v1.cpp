#include <iostream>
#include <string>
#include <sstream>
#include <vector>

class Widget {
public:
    Widget(Widget* parent = nullptr): _parent(parent) {
        if (_parent) _parent->setChildren(this);
    };
    virtual ~Widget() = default;
    virtual void draw() {};
    virtual void draw(std::stringstream&) {};
    virtual void setText(const std::string&) = 0;
    void setChildren(Widget* children = nullptr) {
        if (!children) return;
        _children.push_back(children);
    };

private:
    Widget* _parent;
    std::vector<Widget*> _children;
};

class ListBox : public Widget {
public:
    void draw(std::stringstream&) override;
private:
    std::vector<std::string> _items;
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
    void draw(std::stringstream&) override;
private:
    std::string _text;
};

class TextBox : public Widget {
public:
    void draw(std::stringstream&) override;
private:
    std::string _text;
};

struct TT { 
    ~TT() {
        std::cout << "TT::destructor\n";
    }
    void operator delete(void *p) {
        std::cout << "TT::operator delete\n";
        free(p);
    }
    int i;
};

int main(int argc, char **argv) {
    TT* tt = new TT();
    delete tt;
    TT tt2;
    delete &tt2;
    return 0;
}
