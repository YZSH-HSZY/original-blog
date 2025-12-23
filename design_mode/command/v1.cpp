#include <iostream>

class Command {
public:
    virtual ~Command() = default;
    virtual void Execute() = 0;
protected:
    Command() = default;
};

class PasteCommand : public Command {
public:
    using Document = struct {void Paste() {std::cout << "Paste\n"; };};
    PasteCommand(Document* document): _document(document) {}
    virtual void Execute() {
        _document->Paste();
    }
private:
    Document* _document;
};

template <class Receiver>
class SimpleCommand : public Command {
public:
    typedef void (Receiver::*Action)();
    SimpleCommand(Receiver* receiver, Action action) : _receiver(receiver), _action(action) {}
    virtual void Execute();
private:
    Action _action;
    Receiver* _receiver;
};

template <class Receiver>
void SimpleCommand<Receiver>::Execute() {
    (_receiver->*_action)();
}

class EasyReceiver {
public:
    void Click() {
        std::cout << "Click\n";
    }
};

int main(int argc, char **argv) {

    EasyReceiver receiver;
    SimpleCommand<EasyReceiver> command(&receiver, &EasyReceiver::Click);
    command.Execute();

    return 0;
}