# cpu的序列号获取

> 参考文档:
> - [知乎-armv8](https://zhuanlan.zhihu.com/p/234822747)

## example

### armv8架构的cpuinfo获取

1. `/proc/cpuinfo`
2. 使用汇编指令, 如下所示:
```c
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <arpa/inet.h>
#include <unistd.h>
#include <string>
#include <fstream>
#ifdef __aarch64__
#include <asm/hwcap.h>
#endif
#include <sys/auxv.h>

#define get_cpu_ftr(id) ({					\
		unsigned long __val;				\
		asm("mrs %0, "#id : "=r" (__val));		\
         printf("%-20s: 0x%016lx\n", #id, __val);	\
		})
		//printf("0x%08lx\n", __val);	
		//printf("%-20s: 0x%016lx\n", #id, __val);	

 
static bool get_cpu_id_by_asm(std::string & cpu_id)
{
    cpu_id.clear();
 
    unsigned int s1 = 0;
    unsigned int s2 = 0;
#if defined(__x86_64__) || defined(__i386__)
    asm volatile
    (
        "movl $0x01, %%eax; \n\t"
        "xorl %%edx, %%edx; \n\t"
        "cpuid; \n\t"
        "movl %%edx, %0; \n\t"
        "movl %%eax, %1; \n\t"
        : "=m"(s1), "=m"(s2)
    );
#elif defined(__aarch64__)
    // ARM64 (需内核权限)
    asm volatile("mrs %0, midr_el1" : "=r"(s1));
    s2 = 0;  // 无对应寄存器
#elif defined(__arm__)
    // ARMv7 (需内核权限)
    asm volatile("mrc p15, 0, %0, c0, c0, 0" : "=r"(s1));
    s2 = 0;
#endif  // machine arch judge

    if (0 == s1 && 0 == s2) return(false);
    char cpu[32] = { 0 };
    snprintf(cpu, sizeof(cpu), "%08X%08X", htonl(s2), htonl(s1));
    std::string(cpu).swap(cpu_id);
 
    return(true);
}
// get_cpu_ftr(ID_AA64ISAR0_EL1);
// get_cpu_ftr(ID_AA64ISAR1_EL1);
// get_cpu_ftr(ID_AA64MMFR0_EL1);
// get_cpu_ftr(ID_AA64MMFR1_EL1);
// get_cpu_ftr(ID_AA64PFR0_EL1);
// get_cpu_ftr(ID_AA64PFR1_EL1);
// get_cpu_ftr(ID_AA64DFR0_EL1);
// get_cpu_ftr(ID_AA64DFR1_EL1);
// get_cpu_ftr(MIDR_EL1);
// get_cpu_ftr(MPIDR_EL1);
// get_cpu_ftr(REVIDR_EL1);
```

 