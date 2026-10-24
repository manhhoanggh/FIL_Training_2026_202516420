# Performance Analysis Methodology

### A performance analysis methodology is a procedure that you can follow to analyze system or application performance.

### Here are some Methodologies:

### 1. Ad Hoc Checklist Method
- Greedy-like working.

### 2. Problem Statement Method
- State questions to trace back the reasons.
- E.g: why u think there is problem, what changed recently, is it latency or runtime, ...

### 3. RTFM Method
- Read The Fine Manual
- Search for Man pages, Books, Web search, Co-workers, Material, ...

### 4. Scientific Method
- Question - Hypothesis - Prediction - Test - Analysis

### 5. OODA Loop
- Observe - Orient - Decide - Act

### 6. Workload Characterization Method
- Analyzing the demands placed on a system/network/application to understand its behavior, performance, and resource requirements (Who/Why/What/How)

### 7. Drill-Down Analysis Method
- Breaks high-level, summarized information into increasingly detailed components.

### 8. Process of Elimination
- Identifies a correct answer/solution by crossing out wrong choice.

### 9. Time Division Method
- Divide to find latency origin.

### 10. 5 Whys Performance Method
- Repeatedly ask "why" to trace subsequent questions or solution.

### 11. By-Layer Method
- Investigate the lowest layer that latency is introduced (Syscalls, network, device drivers, ...)

### 12. Tools Method
- Analyze and choose the most useful metrics in each tool to address prob.

### 13. USE Method
- Check Utilization, Saturation and Errors for every resource.

### 14. RED Method
- For every service or microservice, check Request rate, Errors, Duration.

### 15. CPU Profile Method
- Understand all software in CPU profile > 1%

### 16. Off-CPU Analysis
- Measures the time threads spend blocked, waiting, or idle rather than executing instructions on the CPU

### 17. Stack Profile Method
- Records the complete code path (stack trace) that led to the thread being descheduled.

### 18. TSA Method
- For each thread of interest, measure time in operating system thread states. (Executing, Runnable, Swapping, ...)
- Investigate states from most to least frequent.

### 19. Active Benchmarking Method
- Configure the benchmark to run for a long duration.
- While running, analyze performance using other tools, and determine limiting factors.

### 20. Method R
- Decide to fix or maintain based on economy.

### 21. Performance Evaluation Steps
- Utilize Method R with 10 scientific steps.

### 22. Capacity Planning Process
- Actively gathering and predicting system performance to achieve best solution with least cost.

### 23. Intel Hierarchical Top-Down Performance Characterization Methodology
- Solve problem by analyzing the execution of uOPs (micro-operations - RISC)

### 24. Problem Mantras
- Magically work! Try changing frequency, method, time.


### 25. Benchmarking Checklist
- List refuting questions to ensure the validity and consistency of the problem.



