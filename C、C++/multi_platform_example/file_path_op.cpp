#include <stdio.h>
#include <string.h>

#ifdef _WIN32
#include <windows.h>
#define PATH_SEP '\\'
#else
#include <libgen.h> // 仅 Linux/macOS 提供 dirname()
#include <unistd.h>
#include <limits.h>
#define PATH_SEP '/'
#endif

// 获取当前执行文件的路径
char* getExecutablePath() {
    static char path[1024];
#ifdef _WIN32
    GetModuleFileName(NULL, path, sizeof(path));
#else
    ssize_t len = readlink("/proc/self/exe", path, sizeof(path) - 1);
    if (len == -1) return NULL;
    path[len] = '\0';
#endif
    return path;
}

// 获取上一级目录
char* getParentDir(const char* path) {
    static char parent[1024];
    strcpy(parent, path);

#ifdef _WIN32
    // Windows: 手动查找最后一个 '\' 并截断
    char* last_sep = strrchr(parent, PATH_SEP);
    if (last_sep) *last_sep = '\0';
#else
    // Linux/macOS: 使用 dirname() 函数
    char* dir = dirname(parent);
    strcpy(parent, dir);
#endif

    return parent;
}

int main() {
    char* exePath = getExecutablePath();
    if (!exePath) {
        printf("Failed to get executable path.\n");
        return 1;
    }

    char* parentDir = getParentDir(exePath);
    printf("Executable path: %s\n", exePath);
    printf("Parent directory: %s\n", parentDir);

    return 0;
}