# DTLS(Datagram Transport Layer Security, 数据包传输层安全)
DTLS是用于UDP数据包传输安全的协议, 已有的TLS不能用来保证UDP上传输的数据的安全，因此Datagram TLS试图在现存的TLS协议架构上提出扩展, 使之支持UDP，即成为TLS的一个支持数据包传输的版本.

> `DTLS 1.0`基于 `TLS 1.1`, `DTLS 1.2` 基于`TLS 1.2`.

## protocol format

参[rfc-TLS1.2](https://www.rfc-editor.org/rfc/rfc5246)
参[rfc-DTLS1.2](https://www.rfc-editor.org/rfc/rfc6347)

```c
// Fragmentation
enum {
    change_cipher_spec(20), alert(21), handshake(22),
    application_data(23), (255)
} ContentType;
// Record Layer
struct {
    ContentType type;
    ProtocolVersion version;
    uint16 epoch;                                     // New field
    uint48 sequence_number;                           // New field
    uint16 length;
    opaque fragment[DTLSPlaintext.length];
} DTLSPlaintext;

struct {
    ContentType type;
    ProtocolVersion version;
    uint16 epoch;                                     // New field
    uint48 sequence_number;                           // New field
    uint16 length;
    opaque fragment[DTLSCompressed.length];
} DTLSCompressed;

struct {
    ContentType type;
    ProtocolVersion version;
    uint16 epoch;                                     // New field
    uint48 sequence_number;                           // New field
    uint16 length;
    select (CipherSpec.cipher_type) {
        case block:  GenericBlockCipher;
        case aead:   GenericAEADCipher;                 // New field
    } fragment;
} DTLSCiphertext;

// Handshake Protocol
enum {
    hello_request(0), client_hello(1), server_hello(2),
    hello_verify_request(3),                          // New field
    certificate(11), server_key_exchange (12),
    certificate_request(13), server_hello_done(14),
    certificate_verify(15), client_key_exchange(16),
    finished(20), (255) } HandshakeType;

struct {
    HandshakeType msg_type;
    uint24 length;
    uint16 message_seq;                               // New field
    uint24 fragment_offset;                           // New field
    uint24 fragment_length;                           // New field
    select (HandshakeType) {
        case hello_request: HelloRequest;
        case client_hello:  ClientHello;
        case server_hello:  ServerHello;
        case hello_verify_request: HelloVerifyRequest;  // New field
        case certificate:Certificate;
        case server_key_exchange: ServerKeyExchange;
        case certificate_request: CertificateRequest;
        case server_hello_done:ServerHelloDone;
        case certificate_verify:  CertificateVerify;
        case client_key_exchange: ClientKeyExchange;
        case finished: Finished;
    } body; 
} Handshake;

struct {
    ProtocolVersion client_version;
    Random random;
    SessionID session_id;
    opaque cookie<0..2^8-1>;                             // New field
    CipherSuite cipher_suites<2..2^16-1>;
    CompressionMethod compression_methods<1..2^8-1>; 
} ClientHello;

struct {
    ProtocolVersion server_version;
    opaque cookie<0..2^8-1>; 
} HelloVerifyRequest;
```