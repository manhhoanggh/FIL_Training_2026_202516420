# FIFOs

### 1. Definition
- A **FIFO** ("First In, First Out") is a **named pipe**.
- FIFOs allow **unrelated processes** to communicate simply by opening the FIFO file by name (no `fork()` required).

### 2. Creation
- **`mkfifo()`** system call:
  `mkfifo("myfifo", 0644);`
- **Permissions**: (e.g., `0644` for `rw-r--r--`).
- **Historical Note**: Formerly created via `mknod(path, S_IFIFO | mode, 0)`.
- Create from cmd: `mkfifo myfifo`.

### 3. Producers and Consumers (Blocking Behavior)
- **Opening a FIFO**: Require both senders and receivers connected to unblock.
- **EOF & Broken Pipe**:
  - All writers close their descriptors -> `read()` call returns `0` (EOF).
  - All readers close their descriptors -> `write()`, raises **`SIGPIPE`** ("Broken Pipe").

### 4. Non-Blocking I/O (`O_NDELAY` / `O_NONBLOCK`)
  - `open(path, O_WRONLY | O_NDELAY)` returns `-1`.
  - `read()` returns `0`.

### 5. Atomic Writes & Data Interleaving
- **Atomic Writes**: Writes up to **`PIPE_BUF`** bytes will not be interleaved.
- **Read Framing**: Even with atomic writes, bare `read()` calls may return partial chunks or combined data .

---

## C Code Implementations

### Example 1: Producer Process (`speak.c`)

```c

    char s;
    int num, fd;

    mkfifo(FIFO_NAME, 0644)
    fd = open(FIFO_NAME, O_WRONLY);

    while (fgets(s, sizeof(s), stdin) != NULL) {
        int len = strlen(s);

        num = write(fd, s, strlen(s))
        printf("speak: wrote %d bytes\n", num);

    close(fd);
    return 0;
```

### Example 2: Consumer Process (tick.c)
```c

    char s;
    int num, fd;

    mkfifo(FIFO_NAME, 0644)
    fd = open(FIFO_NAME, O_RDONLY);

    do {
        num = read(fd, s, sizeof(s) - 1)
        if (num > 0) {
            s[num] = '\0';
            printf("tick: read %d bytes: \"%s\"\n", num, s);
        }
    } while (num > 0);

    printf("tick: writer closed connection\n");
    close(fd);
    return 0;
}
