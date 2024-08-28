Microsoft Windows [版本 10.0.19042.1766]
(c) Microsoft Corporation。保留所有权利。

E:\AndroidSDK\emulator>emulator.exe -h
INFO | Android emulator version 31.3.11.0 (build_id 9058569) (CL:N/A)
ERROR | No AVD specified. Use '@foo' or '-avd foo' to launch a virtual device named 'foo'

E:\AndroidSDK\emulator>emulator.exe --help
Android Emulator usage: emulator [options] [-qemu args]
options:
-list-avds list ava ilable AVDs
-sysdir <dir> search f or system disk images in <dir>
-system <file> read ini tial system image from <file>
-vendor <file> read ini tial vendor image from <file>
-writable-system make sys tem & vendor image writable after 'adb remount'
-delay-adb delay ad b communication till boot completes
-datadir <dir> write us er data into <dir>
-kernel <file> use spec ific emulated kernel
-ramdisk <file> ramdisk image (default <system>/ramdisk.img
-image <file> obsolete , use -system <file> instead
-initdata <file> same as '-init-data <file>'
-data <file> data ima ge (default <datadir>/userdata-qemu.img
-encryption-key <file> read ini tial encryption key image from <file>
-logcat-output <file> output f ile of logcat(default none)
-partition-size <size> system/d ata partition size in MBs
-cache <file> cache pa rtition image (default is temporary file)
-cache-size <size> cache pa rtition size in MBs
-no-cache disable the cache partition
-nocache same as -no-cache
-sdcard <file> SD card image (default <datadir>/sdcard.img
-quit-after-boot <timeout> qeuit em ulator after guest boots completely, or after timeout in seconds
-qemu-top-dir <dir> Use the emulator in the specified dir (relative or absolute path)
-monitor-adb <verbose_level> monitor the adb messages between guest and host, default not
-snapstorage <file> file tha t contains all state snapshots (default <datadir>/snapshots.img)
-no-snapstorage do not m ount a snapshot storage file (this disables all snapshot functionality)
-snapshot <name> name of snapshot within storage file for auto-start and auto-save (default 'default-boot ')
-no-snapshot perform a full boot and do not auto-save, but qemu vmload and vmsave operate on snapstor age
-no-snapshot-save do not a uto-save to snapshot on exit: abandon changed state
-no-snapshot-load do not a uto-start from snapshot: perform a full boot
-snapshot-list show a l ist of available snapshots
-no-snapshot-update-time do not t ry to correct snapshot time on restore
-wipe-data reset th e user data image (copy it from initdata)
-avd <name> use a sp ecific android virtual device
-avd-arch <target> use a sp ecific target architecture
-skindir <dir> search s kins in <dir> (default <system>/skins)
-skin <name> select a given skin
-no-skin deprecat ed: create an AVD with no skin instead
-noskin same as -no-skin
-memory <size> physical RAM size in MBs
-ui-only <UI feature> run only the UI feature requested
-id <name> assign a n id to this virtual device (separate from the avd name)
-cores <number> Set numb er of CPU cores to emulator
-accel <mode> Configur e emulation acceleration
-no-accel Same as '-accel off'
-ranchu Use new emulator backend instead of the classic one
-engine <engine> Select e ngine. auto|classic|qemu2
-netspeed <speed> maximum network download/upload speeds
-netdelay <delay> network latency emulation
-netfast disable network shaping
-code-profile <name> enable c ode profiling
-show-kernel display kernel messages
-shell enable r oot shell on current terminal
-no-jni deprecat ed, see dalvik_vm_checkjni
-nojni deprecat ed, see dalvik_vm_checkjni
-dalvik-vm-checkjni Enable d alvik.vm.checkjni
-logcat <tags> enable l ogcat output with given tags
-log-nofilter Disable the duplicate log filter
-no-audio disable audio support
-noaudio same as -no-audio
-audio <backend> use spec ific audio backend
-radio <device> redirect radio modem interface to character device
-port <port> TCP port that will be used for the console
-ports <consoleport>,<adbport> TCP port s used for the console and adb bridge
-modem-simulator-port <port> TCP port that will be used for android modem simulator
-onion <image> use over lay PNG image over screen
-onion-alpha <%age> specify onion-skin translucency
-onion-rotation 0|1|2|3 specify onion-skin rotation
-dpi-device <dpi> specify device's resolution in dpi (default DEFAULT_DEVICE_DPI)
-scale <scale> scale em ulator window (deprecated)
-wifi-client-port <port> connect to other emulator for WiFi forwarding
-wifi-server-port <port> listen t o other emulator for WiFi forwarding
-http-proxy <proxy> make TCP connections through a HTTP/HTTPS proxy
-timezone <timezone> use this timezone instead of the host's default
-change-language <language> use this language instead of the current one. Restarts the framework.
-change-country <country> use this country instead of the current one. Restarts the framework.
-change-locale <locale> use this locale instead of the current one. Restarts the framework.
-dns-server <servers> use this DNS server(s) in the emulated system
-net-tap <interface> use this TAP interface for networking
-net-tap-script-up <script> script t o run when the TAP interface goes up
-net-tap-script-down <script> script t o run when the TAP interface goes down
-cpu-delay <cpudelay> throttle CPU emulation
-no-boot-anim disable animation for faster boot
-no-window disable graphical window display
-qt-hide-window Start QT window but hide window display
-no-sim device h as no SIM card
-lowram device i s a low ram device
-version display emulator version number
-no-passive-gps disable passive gps updates
-gnss-file-path <path> Use the specified filepath to read gnss data
-gnss-grpc-port <port number> Use the specified port number to start grpc service to receive gnss data
-virtio-console using vi rtio console as console
-read-only allow ru nning multiple instances of emulators on the same AVD, but cannot save snapshot.  
 -is-restart <restart-pid> specifie s that this emulator was a restart, and to wait out <restart-pid> before proceed ing
-report-console <socket> report c onsole port to remote socket
-gps <device> redirect NMEA GPS to character device
-shell-serial <device> specific character device for root shell
-tcpdump <file> capture network packets to file
-bootchart <timeout> enable b ootcharting
-charmap <file> use spec ific key character map
-studio-params <file> used by Android Studio to provide parameters
-prop <name>=<value> set syst em property on boot
-shared-net-id <number> join the shared network, using IP address 10.1.2.<number>
-gpu <mode> set hard ware OpenGLES emulation mode
-use-host-vulkan use host for vulkan emulation regardless of 'gpu' mode
-camera-back <mode> set emul ation mode for a camera facing back
-camera-front <mode> set emul ation mode for a camera facing front
-webcam-list lists we b cameras available for emulation
-virtualscene-poster <name>=<filename> Load a p ng or jpeg image as a poster in the virtual scene
-screen <mode> set emul ated screen mode
-force-32bit always u se 32-bit emulator
-selinux <disabled|permissive> Set SELi nux to either disabled or permissive mode
-unix-pipe <path> Add <pat                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        h> to the list of allowed Unix pipes
-fixed-scale Use fixe d 1:1 scale for the initial emulator window.
-wait-for-debugger Pause on launch and wait for a debugger process to attach before resuming
-skip-adb-auth Skip adb authentication dialogue
-metrics-to-console Enable u sage metrics and print the messages to stdout
-metrics-collection Enable u sage metrics and send them to google play
-metrics-to-file <file> Enable u sage metrics and write the messages into specified file
-detect-image-hang Enable t he detection of system image hangs.
-feature <name|-name> Force-en able or disable (-name) the features
-icc-profile <file> Use icc profile from specified file
-sim-access-rules-file <file> Use SIM access rules from specified file
-phone-number <phone_number> Sets the phone number of the emulated device
-acpi-config <file> specify acpi device proprerties (hierarchical key=value pair)
-fuchsia Run Fuch sia image. Bypasses android-specific setup; args after are treated as standard Q EMU args
-window-size <size> Set wind ow size for when bypassing android-specific setup.
-allow-host-audio Allows s ending of audio from audio input devices. Otherwise, zeroes out audio.
-restart-when-stalled Allows r estarting guest when it is stalled.
-perf-stat <file> Run peri odic perf stat reporter in the background and write output to specified file.
-share-vid Share cu rrent video state in shared memory region.
-grpc <port> TCP port s used for the gRPC bridge.
-grpc-tls-key <pem> File wit h the private key used to enable gRPC TLS.
-grpc-tls-cer <pem> File wit h the public X509 certificate used to enable gRPC TLS.
-grpc-tls-ca <pem> File wit h the Certificate Authorities used to validate client certificates.
-grpc-use-token Use the emulator console token for gRPC authentication.
-grpc-use-jwt Use a si gned JWT token for gRPC authentication.
-idle-grpc-timeout <timeout> Terminat e the emulator if there is no gRPC activity within <timeout> seconds.
-waterfall <mode> Mode in which to run waterfall.
-rootcanal-hci-port <port> Rootcana l virtual hci port.
-rootcanal-test-port <port> Rootcana l testing port.
-rootcanal-link-port <port> Rootcana l link layer port. <DEPRECATED>
-rootcanal-link-ble-port <port> Rootcana l link ble layer port. <DEPRECATED>
-rootcanal-controller-properties <file> Rootcanal con troller_properties.json file.
-rootcanal-default-commands-file <file> Rootcana l commands file to run on launch.
-rootcanal-no-mesh Disable auto discovery and connection bluetooth enabled emulators
-forward-vhci Enable t he VHCI grpc forwarding service.
-multidisplay index width height dpi flag config m ultiple displays.
-google-maps-key <API key> API key to use with the Google Maps GUI.
-no-location-ui Disable the location UI in the extended window.
-use-keycode-forwarding Use keyc ode forwarding instead of host charmap translation.
-record-session <file>,<delay>[,<duration>] Screen r ecord the emulator session.
-legacy-fake-camera Use lega cy camera HAL for the emulated fake camera.
-camera-hq-edge Enable h igh qualify edge processing for emulated camera.
-no-direct-adb Use exte rnal adb executable for internal communication.
-check-snapshot-loadable <snapshot name|exported snapshot tar file> Check if a snasphot is loadable.
-no-hidpi-scaling Disable HiDPI scaling of guest display on macOS devices.
-no-mouse-reposition Do not r eposition the mouse to emulator window center if mouse pointer gets out of the w indow.
-guest-angle Enable g uest ANGLE as system driver.
-usb-passthrough VID PID BUS PORTS Host USB device Passthrough
-append-userspace-opt key=value Appends a property which is passed to the userspace.
-save-path <file path> Override save path for screenshot and bug report. The value will not be persisted on hos t OS.
-no-nested-warnings Disable the warning dialog when emulator is running in nested virtualization.
-wifi-tap <interface> use this TAP interface for Virtio Wi-Fi
-wifi-tap-script-up <script> script t o run when the TAP interface goes up
-wifi-tap-script-down <script> script t o run when the TAP interface goes down
-wifi-vmnet <interface> This op tion is alias to vmnet, it is used for backward compatibility.
-vmnet <interface> Use thi s network <interface> and enable vmnet framework as the backend of tap netdev on MacOS.

     -qemu args...                                                      pass arg                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        uments to qemu
     -qemu -h                                                           display                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         qemu help

     -verbose                                                           same as                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         '-debug-init'
     -debug <tags>                                                      enable/d                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        isable debug messages
     -debug-<tag>                                                       enable s                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        pecific debug messages
     -debug-no-<tag>                                                    disable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         specific debug messages

     -help                                                              print th                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        is help
     -help-<option>                                                     print op                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        tion-specific help

     -help-disk-images                                                  about di                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        sk images
     -help-debug-tags                                                   debug ta                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        gs for -debug <tags>
     -help-char-devices                                                 characte                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        r <device> specification
     -help-environment                                                  environm                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ent variables
     -help-virtual-device                                               virtual                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         device management
     -help-sdk-images                                                   about di                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        sk images when using the SDK
     -help-build-images                                                 about di                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        sk images when building Android
     -help-all                                                          prints a                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ll help content

E:\AndroidSDK\emulator>emulator.exe -list-avds
Pixel_5_API_25

E:\AndroidSDK\emulator>emulator.exe -list-avds
Pixel_5_API_25

E:\AndroidSDK\emulator>emulator.exe --help
Android Emulator usage: emulator [options] [-qemu args]
options:
-list-avds list available AVDs
-sysdir <dir> search for system disk images in <dir>
-system <file> read initial system image from <file>
-vendor <file> read initial vendor image from <file>
-writable-system make system & vendor image writable after 'adb remount'
-delay-adb delay adb communication till boot completes
-datadir <dir> write user data into <dir>
-kernel <file> use specific emulated kernel
-ramdisk <file> ramdisk image (default <system>/ramdisk.img
-image <file> obsolete, use -system <file> instead
-initdata <file> same as '-init-data <file>'
-data <file> data image (default <datadir>/userdata-qemu.img
-encryption-key <file> read initial encryption key image from <file>
-logcat-output <file> output file of logcat(default none)
-partition-size <size> system/data partition size in MBs
-cache <file> cache partition image (default is temporary file)
-cache-size <size> cache partition size in MBs
-no-cache disable the cache partition
-nocache same as -no-cache
-sdcard <file> SD card image (default <datadir>/sdcard.img
-quit-after-boot <timeout> qeuit emulator after guest boots completely, or after timeout in seconds
-qemu-top-dir <dir> Use the emulator in the specified dir (relative or absolute path)
-monitor-adb <verbose_level> monitor the adb messages between guest and host, default not
-snapstorage <file> file that contains all state snapshots (default <datadir>/snapshots.img)
-no-snapstorage do not mount a snapshot storage file (this disables all snapshot functionality)
-snapshot <name> name of snapshot within storage file for auto-start and auto-save (default 'default-boot')
-no-snapshot perform a full boot and do not auto-save, but qemu vmload and vmsave operate on snapstorage
-no-snapshot-save do not auto-save to snapshot on exit: abandon changed state
-no-snapshot-load do not auto-start from snapshot: perform a full boot
-snapshot-list show a list of available snapshots
-no-snapshot-update-time do not try to correct snapshot time on restore
-wipe-data reset the user data image (copy it from initdata)
-avd <name> use a specific android virtual device
-avd-arch <target> use a specific target architecture
-skindir <dir> search skins in <dir> (default <system>/skins)
-skin <name> select a given skin
-no-skin deprecated: create an AVD with no skin instead
-noskin same as -no-skin
-memory <size> physical RAM size in MBs
-ui-only <UI feature> run only the UI feature requested
-id <name> assign an id to this virtual device (separate from the avd name)
-cores <number> Set number of CPU cores to emulator
-accel <mode> Configure emulation acceleration
-no-accel Same as '-accel off'
-ranchu Use new emulator backend instead of the classic one
-engine <engine> Select engine. auto|classic|qemu2
-netspeed <speed> maximum network download/upload speeds
-netdelay <delay> network latency emulation
-netfast disable network shaping
-code-profile <name> enable code profiling
-show-kernel display kernel messages
-shell enable root shell on current terminal
-no-jni deprecated, see dalvik_vm_checkjni
-nojni deprecated, see dalvik_vm_checkjni
-dalvik-vm-checkjni Enable dalvik.vm.checkjni
-logcat <tags> enable logcat output with given tags
-log-nofilter Disable the duplicate log filter
-no-audio disable audio support
-noaudio same as -no-audio
-audio <backend> use specific audio backend
-radio <device> redirect radio modem interface to character device
-port <port> TCP port that will be used for the console
-ports <consoleport>,<adbport> TCP ports used for the console and adb bridge
-modem-simulator-port <port> TCP port that will be used for android modem simulator
-onion <image> use overlay PNG image over screen
-onion-alpha <%age> specify onion-skin translucency
-onion-rotation 0|1|2|3 specify onion-skin rotation
-dpi-device <dpi> specify device's resolution in dpi (default DEFAULT_DEVICE_DPI)
-scale <scale> scale emulator window (deprecated)
-wifi-client-port <port> connect to other emulator for WiFi forwarding
-wifi-server-port <port> listen to other emulator for WiFi forwarding
-http-proxy <proxy> make TCP connections through a HTTP/HTTPS proxy
-timezone <timezone> use this timezone instead of the host's default
-change-language <language> use this language instead of the current one. Restarts the framework.
-change-country <country> use this country instead of the current one. Restarts the framework.
-change-locale <locale> use this locale instead of the current one. Restarts the framework.
-dns-server <servers> use this DNS server(s) in the emulated system
-net-tap <interface> use this TAP interface for networking
-net-tap-script-up <script> script to run when the TAP interface goes up
-net-tap-script-down <script> script to run when the TAP interface goes down
-cpu-delay <cpudelay> throttle CPU emulation
-no-boot-anim disable animation for faster boot
-no-window disable graphical window display
-qt-hide-window Start QT window but hide window display
-no-sim device has no SIM card
-lowram device is a low ram device
-version display emulator version number
-no-passive-gps disable passive gps updates
-gnss-file-path <path> Use the specified filepath to read gnss data
-gnss-grpc-port <port number> Use the specified port number to start grpc service to receive gnss data
-virtio-console using virtio console as console
-read-only allow running multiple instances of emulators on the same AVD, but cannot save snapshot.
-is-restart <restart-pid> specifies that this emulator was a restart, and to wait out <restart-pid> before proceeding
-report-console <socket> report console port to remote socket
-gps <device> redirect NMEA GPS to character device
-shell-serial <device> specific character device for root shell
-tcpdump <file> capture network packets to file
-bootchart <timeout> enable bootcharting
-charmap <file> use specific key character map
-studio-params <file> used by Android Studio to provide parameters
-prop <name>=<value> set system property on boot
-shared-net-id <number> join the shared network, using IP address 10.1.2.<number>
-gpu <mode> set hardware OpenGLES emulation mode
-use-host-vulkan use host for vulkan emulation regardless of 'gpu' mode
-camera-back <mode> set emulation mode for a camera facing back
-camera-front <mode> set emulation mode for a camera facing front
-webcam-list lists web cameras available for emulation
-virtualscene-poster <name>=<filename> Load a png or jpeg image as a poster in the virtual scene
-screen <mode> set emulated screen mode
-force-32bit always use 32-bit emulator
-selinux <disabled|permissive> Set SELinux to either disabled or permissive mode
-unix-pipe <path> Add <path> to the list of allowed Unix pipes
-fixed-scale Use fixed 1:1 scale for the initial emulator window.
-wait-for-debugger Pause on launch and wait for a debugger process to attach before resuming
-skip-adb-auth Skip adb authentication dialogue
-metrics-to-console Enable usage metrics and print the messages to stdout
-metrics-collection Enable usage metrics and send them to google play
-metrics-to-file <file> Enable usage metrics and write the messages into specified file
-detect-image-hang Enable the detection of system image hangs.
-feature <name|-name> Force-enable or disable (-name) the features
-icc-profile <file> Use icc profile from specified file
-sim-access-rules-file <file> Use SIM access rules from specified file
-phone-number <phone_number> Sets the phone number of the emulated device
-acpi-config <file> specify acpi device proprerties (hierarchical key=value pair)
-fuchsia Run Fuchsia image. Bypasses android-specific setup; args after are treated as standard QEMU args
-window-size <size> Set window size for when bypassing android-specific setup.
-allow-host-audio Allows sending of audio from audio input devices. Otherwise, zeroes out audio.
-restart-when-stalled Allows restarting guest when it is stalled.
-perf-stat <file> Run periodic perf stat reporter in the background and write output to specified file.
-share-vid Share current video state in shared memory region.
-grpc <port> TCP ports used for the gRPC bridge.
-grpc-tls-key <pem> File with the private key used to enable gRPC TLS.
-grpc-tls-cer <pem> File with the public X509 certificate used to enable gRPC TLS.
-grpc-tls-ca <pem> File with the Certificate Authorities used to validate client certificates.
-grpc-use-token Use the emulator console token for gRPC authentication.
-grpc-use-jwt Use a signed JWT token for gRPC authentication.
-idle-grpc-timeout <timeout> Terminate the emulator if there is no gRPC activity within <timeout> seconds.
-waterfall <mode> Mode in which to run waterfall.
-rootcanal-hci-port <port> Rootcanal virtual hci port.
-rootcanal-test-port <port> Rootcanal testing port.
-rootcanal-link-port <port> Rootcanal link layer port. <DEPRECATED>
-rootcanal-link-ble-port <port> Rootcanal link ble layer port. <DEPRECATED>
-rootcanal-controller-properties <file> Rootcanal controller_properties.json file.
-rootcanal-default-commands-file <file> Rootcanal commands file to run on launch.
-rootcanal-no-mesh Disable auto discovery and connection bluetooth enabled emulators
-forward-vhci Enable the VHCI grpc forwarding service.
-multidisplay index width height dpi flag config multiple displays.
-google-maps-key <API key> API key to use with the Google Maps GUI.
-no-location-ui Disable the location UI in the extended window.
-use-keycode-forwarding Use keycode forwarding instead of host charmap translation.
-record-session <file>,<delay>[,<duration>] Screen record the emulator session.
-legacy-fake-camera Use legacy camera HAL for the emulated fake camera.
-camera-hq-edge Enable high qualify edge processing for emulated camera.
-no-direct-adb Use external adb executable for internal communication.
-check-snapshot-loadable <snapshot name|exported snapshot tar file> Check if a snasphot is loadable.
-no-hidpi-scaling Disable HiDPI scaling of guest display on macOS devices.
-no-mouse-reposition Do not reposition the mouse to emulator window center if mouse pointer gets out of the window.
-guest-angle Enable guest ANGLE as system driver.
-usb-passthrough VID PID BUS PORTS Host USB device Passthrough
-append-userspace-opt key=value Appends a property which is passed to the userspace.
-save-path <file path> Override save path for screenshot and bug report. The value will not be persisted on host OS.
-no-nested-warnings Disable the warning dialog when emulator is running in nested virtualization.
-wifi-tap <interface> use this TAP interface for Virtio Wi-Fi
-wifi-tap-script-up <script> script to run when the TAP interface goes up
-wifi-tap-script-down <script> script to run when the TAP interface goes down
-wifi-vmnet <interface> This option is alias to vmnet, it is used for backward compatibility.
-vmnet <interface> Use this network <interface> and enable vmnet framework as the backend of tap netdev on MacOS.

     -qemu args...                                                      pass arguments to qemu
     -qemu -h                                                           display qemu help

     -verbose                                                           same as '-debug-init'
     -debug <tags>                                                      enable/disable debug messages
     -debug-<tag>                                                       enable specific debug messages
     -debug-no-<tag>                                                    disable specific debug messages

     -help                                                              print this help
     -help-<option>                                                     print option-specific help

     -help-disk-images                                                  about disk images
     -help-debug-tags                                                   debug tags for -debug <tags>
     -help-char-devices                                                 character <device> specification
     -help-environment                                                  environment variables
     -help-virtual-device                                               virtual device management
     -help-sdk-images                                                   about disk images when using the SDK
     -help-build-images                                                 about disk images when building Android
     -help-all                                                          prints all help content

E:\AndroidSDK\emulator>emulator.exe -list-avds
Pixel_5_API_25

E:\AndroidSDK\emulator>emulator.exe -avd Pixel*5_API_25
INFO | Android emulator version 31.3.11.0 (build_id 9058569) (CL:N/A)
emulator: INFO: Found systemPath E:\AndroidSDK\system-images\android-25\google_apis\x86\
emulator: INFO: Found systemPath E:\AndroidSDK\system-images\android-25\google_apis\x86\
INFO | Duplicate loglines will be removed, if you wish to see each indiviudal line launch with the -log-nofilter flag.
INFO | IPv4 server found: 192.168.144.64
INFO | configAndStartRenderer: setting vsync to 60 hz
INFO | added library vulkan-1.dll
HAX is working and emulator runs in fast virt mode.
WARNING | \*\** No gRPC protection active, consider launching with the -grpc-use-jwt flag.\_\*\*
INFO | Started GRPC server at 127.0.0.1:8554, security: Local, auth: none
INFO | Advertising in: C:\Users\USER\AppData\Local\Temp\avd\running\pid_11580.ini
INFO | setDisplayConfigs w 1080 h 2340 dpiX 440 dpiY 440
INFO | Your emulator is out of date, please update by launching Android Studio:

- Start Android Studio
- Select menu "Tools > Android > SDK Manager"
- Click "SDK Tools" tab
- Check "Android Emulator" checkbox
- Click "OK"

INFO | Critical: Uncaught ReferenceError: $ is not defined (qrc:/html/js/location-loader.js:1, (null))

[11580:8924:0628/114712.679:ERROR:ssl_client_socket_impl.cc(1050)] handshake failed; returned -1, SSL error code 1, net_error -101
INFO | Wait for emulator (pid 11580) 20 seconds to shutdown gracefully before kill;you can set environment variable ANDROID_EMULATOR_WAIT_TIME_BEFORE_KILL(in seconds) to change the default value (20 seconds)

INFO | Wait for emulator (pid 11580) 20 seconds to shutdown gracefully before kill;you can set environment variable ANDROID_EMULATOR_WAIT_TIME_BEFORE_KILL(in seconds) to change the default value (20 seconds)

E:\AndroidSDK\emulator>emulator.exe -avd Pixel*5_API_25
INFO | Android emulator version 31.3.11.0 (build_id 9058569) (CL:N/A)
emulator: INFO: Found systemPath E:\AndroidSDK\system-images\android-25\google_apis\x86\
emulator: INFO: Found systemPath E:\AndroidSDK\system-images\android-25\google_apis\x86\
INFO | Duplicate loglines will be removed, if you wish to see each indiviudal line launch with the -log-nofilter flag.
INFO | IPv4 server found: 192.168.144.64
INFO | configAndStartRenderer: setting vsync to 60 hz
INFO | added library vulkan-1.dll
HAX is working and emulator runs in fast virt mode.
WARNING | \*\** No gRPC protection active, consider launching with the -grpc-use-jwt flag.\_\*\*
INFO | Started GRPC server at 127.0.0.1:8554, security: Local, auth: none
INFO | Advertising in: C:\Users\USER\AppData\Local\Temp\avd\running\pid_7676.ini
INFO | setDisplayConfigs w 1080 h 2340 dpiX 440 dpiY 440
ERROR | Unable to connect to adb daemon on port: 5037
[7676:10928:0628/115508.062:ERROR:ssl_client_socket_impl.cc(1050)] handshake failed; returned -1, SSL error code 1, net_error -101
[7676:10928:0628/115508.502:ERROR:ssl_client_socket_impl.cc(1050)] handshake failed; returned -1, SSL error code 1, net_error -101
INFO | Critical: Uncaught ReferenceError: $ is not defined (qrc:/html/js/location-loader.js:1, (null))

INFO | Wait for emulator (pid 7676) 20 seconds to shutdown gracefully before kill;you can set environment variable ANDROID_EMULATOR_WAIT_TIME_BEFORE_KILL(in seconds) to change the default value (20 seconds)

INFO | Wait for emulator (pid 7676) 20 seconds to shutdown gracefully before kill;you can set environment variable ANDROID_EMULATOR_WAIT_TIME_BEFORE_KILL(in seconds) to change the default value (20 seconds)

E:\AndroidSDK\emulator>
