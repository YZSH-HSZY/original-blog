#include <iostream>
#include <vector>
// #include <

class Request {
public:
    enum class Type { 
        ARequest, 
        BRequest, 
        CRequest
    };
    virtual ~Request() {}
    virtual Type getType() = 0;
};

class ARequest : public Request {
public:
    Type getType() { return Type::ARequest; }
};

class Handler {
public:
    Handler(Handler *next) : _next(next) {}
    Handler() : _next(nullptr) {}
    virtual ~Handler() = default;
    virtual void handle(Request* request) {
        if (_next) {
            _next->handle(request);
        }
    }
private:
    Handler *_next;
};

class ExtHandler : public Handler {
public:
    void handle(Request* request) {
        if (request->getType() == Request::Type::ARequest) {
            std::cout << "ExtHandler" << std::endl;
        } else {
            Handler::handle(request);
        }
    }
};

int main(int argc, char **argv) {
    
    std::shared_ptr<Handler> extHandler = std::make_shared<ExtHandler>();
    std::shared_ptr<Handler> handler = std::make_shared<Handler>(extHandler.get());
    std::shared_ptr<Request> request = std::make_shared<ARequest>();
    handler->handle(request.get());
    return 0;
}