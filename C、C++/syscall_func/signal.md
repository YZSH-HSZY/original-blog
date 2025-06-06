# signal

## Example

```cpp
#include <signal.h>
static void ProcessExit(int sig) {
    ...
}
signal(SIGINT, ProcessExit);
```