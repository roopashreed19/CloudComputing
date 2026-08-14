# Experiment 6: Simulate a Cloud Scenario Using CloudSim and Run a Custom Scheduling Algorithm

## Aim

To simulate a cloud computing scenario using the CloudSim framework and execute a custom scheduling algorithm that is not available by default in CloudSim.

---

## Objectives

* To understand cloud simulation concepts using the CloudSim framework.
* To set up and configure CloudSim in Eclipse IDE.
* To initialize CloudSim components such as Datacenters, Hosts, VMs, DatacenterBroker, and Cloudlets.
* To define virtual machine allocation and cloudlet scheduling policies.
* To execute a cloud scenario simulation.
* To analyze simulation output such as Start Time, Finish Time, Execution Status, and Debt.

---

## Software & Platform Used

* **IDE:** Eclipse IDE
* **JDK:** Java Development Kit (JDK 8 or higher)
* **Simulation Toolkit:** CloudSim Toolkit (v3.0 / v4.0)
* **Programming Language:** Java

---

## Introduction

CloudSim is a simulation framework used for modeling and simulating cloud computing environments. It allows researchers and developers to create virtualized cloud infrastructure consisting of datacenters, hosts, virtual machines, brokers, and cloudlets.

Using CloudSim, different resource allocation and task scheduling algorithms can be tested without requiring a physical cloud infrastructure.

In this experiment, a basic cloud environment is created and Cloudlets are submitted to virtual machines for execution. The simulation output is then analyzed to understand the behavior of the cloud resources.

---

# Procedure

## Step 1: Download and Extract CloudSim

1. Download the CloudSim Toolkit package.
2. Extract the downloaded ZIP file to a suitable location on the computer.
3. Locate the extracted CloudSim project files and JAR dependencies.

---

## Step 2: Open Eclipse IDE

Launch the **Eclipse IDE** and select the required workspace.

The Eclipse workspace is used to create and execute the Java project containing the CloudSim simulation program.

---

## Step 3: Create a New Java Project

In Eclipse:

**File → New → Java Project**

Enter a suitable project name, for example:

```text
CloudSim_Simulation
```

Click **Finish** to create the project.

---

## Step 4: Import CloudSim into Eclipse

Import the extracted CloudSim project or add the required CloudSim JAR files to the project.

To add the JAR files:

**Right-click Project → Build Path → Configure Build Path → Libraries → Add External JARs**

Select the required CloudSim JAR files and click **Apply and Close**.

The CloudSim libraries are now available to the Java project.

---

## Step 5: Initialize the CloudSim Package

Before creating cloud entities, initialize the CloudSim simulation environment.

```java
int num_user = 1;

Calendar calendar = Calendar.getInstance();

boolean trace_flag = false;

CloudSim.init(num_user, calendar, trace_flag);
```

### Explanation

* `num_user`: Specifies the number of cloud users.
* `Calendar`: Provides the simulation calendar.
* `trace_flag`: Enables or disables event tracing.
* `CloudSim.init()`: Initializes the CloudSim simulation environment.

---

## Step 6: Create the Datacenter

A Datacenter represents a cloud resource provider. It contains physical hosts that provide CPU, memory, bandwidth, and storage resources.

A Datacenter can be created using `DatacenterCharacteristics` and a VM allocation policy.

```java
Datacenter datacenter0 = new Datacenter(
    name,
    characteristics,
    new VmAllocationPolicySimple(hostList),
    storageList,
    0
);
```

### Explanation

The `DatacenterCharacteristics` object contains information about:

* System architecture
* Operating system
* Physical hosts
* VM allocation policy
* Time zone
* Cost information

The `VmAllocationPolicySimple` determines how virtual machines are allocated to available hosts.

---

## Step 7: Create DatacenterBroker

The DatacenterBroker acts as an intermediary between the cloud user and the datacenter.

Create the broker using:

```java
DatacenterBroker broker = createBroker();

int brokerId = broker.getId();
```

The broker is responsible for submitting VMs and Cloudlets to the appropriate cloud resources.

---

## Step 8: Create a Virtual Machine

Create a virtual machine with the required resource parameters.

```java
int vmid = 0;

int mips = 1000;

long size = 10000;

int ram = 512;

long bw = 1000;

int pesNumber = 1;

String vmm = "Xen";

Vm vm = new Vm(
    vmid,
    brokerId,
    mips,
    pesNumber,
    ram,
    bw,
    size,
    vmm,
    new CloudletSchedulerTimeShared()
);

vmlist.add(vm);
```

### Explanation

* `vmid`: Unique ID of the virtual machine.
* `mips`: Million Instructions Per Second assigned to the VM.
* `size`: VM image size in MB.
* `ram`: Memory allocated to the VM.
* `bw`: Bandwidth allocated to the VM.
* `pesNumber`: Number of processing elements/CPU cores.
* `vmm`: Virtual Machine Monitor name.
* `CloudletSchedulerTimeShared`: Scheduling policy used by the VM.

---

## Step 9: Submit the VM List to the Broker

Submit the created VM list to the DatacenterBroker:

```java
broker.submitVmList(vmlist);
```

The broker now has the list of VMs that need to be created in the cloud environment.

---

## Step 10: Create a Cloudlet

A Cloudlet represents a task or application workload that needs to be executed by a virtual machine.

Create a Cloudlet using:

```java
int id = 0;

long length = 400000;

long fileSize = 300;

long outputSize = 300;

UtilizationModel utilizationModel = new UtilizationModelFull();

Cloudlet cloudlet = new Cloudlet(
    id,
    length,
    pesNumber,
    fileSize,
    outputSize,
    utilizationModel,
    utilizationModel,
    utilizationModel
);

cloudlet.setUserId(brokerId);

cloudletList.add(cloudlet);
```

### Explanation

* `id`: Unique Cloudlet ID.
* `length`: Number of instructions that must be executed.
* `fileSize`: Input file size.
* `outputSize`: Output file size.
* `pesNumber`: Number of processing elements required.
* `UtilizationModelFull`: Represents full resource utilization.

---

## Step 11: Submit the Cloudlet List to the Broker

Submit the Cloudlet list to the broker:

```java
broker.submitCloudletList(cloudletList);
```

The broker schedules the Cloudlet for execution on the available VM.

---

## Step 12: Start the CloudSim Simulation

Start the simulation using:

```java
CloudSim.startSimulation();
```

After the simulation has completed, stop the simulation:

```java
CloudSim.stopSimulation();
```

The CloudSim engine processes the events generated by the Datacenter, Broker, VMs, and Cloudlets.

---

# Custom Scheduling Algorithm

CloudSim provides several built-in allocation and scheduling mechanisms. A custom scheduling algorithm can be implemented by modifying or extending the appropriate scheduling or allocation component.

For example, a custom scheduling policy can select a VM based on available processing capacity.

A simple conceptual scheduling approach is:

```text
1. Receive the list of available VMs.
2. Check the processing capacity of each VM.
3. Compare the available MIPS of the VMs.
4. Select the VM with the highest available processing capacity.
5. Assign the Cloudlet to the selected VM.
6. Execute the Cloudlet.
7. Record the execution time and completion time.
```

This allows a scheduling strategy that is different from the default scheduling mechanism to be evaluated through simulation.

---

# Sample Simulation Output

A successful simulation may produce output similar to:

```text
Starting CloudSimExample1...
Initialising...
Starting CloudSim version 3.0
Datacenter_0 is starting...
Broker is starting...
Entities started.

0.0: Broker: Cloud Resource List received with 1 resource(s)

0.0: Broker: Trying to Create VM #0 in Datacenter_0

0.0: Broker: VM #0 has been created in Datacenter #0, Host #0

0.1: Broker: Sending cloudlet 0 to VM #0

400.1: Broker: Cloudlet 0 received

0.1: Broker: All Cloudlets executed. Finishing...

400.1: Broker: Destroying VM #0

Broker is shutting down...

Simulation: No more future events

CloudInformationService: Notify all CloudSim entities for shutting down.

Datacenter_0 is shutting down...

Broker is shutting down...

Simulation completed.

========== OUTPUT ==========

Cloudlet ID    STATUS    Datacenter ID    VM ID    Time    Start Time    Finish Time

0              SUCCESS   2                0        400     0.1           400.1

***** Datacenter: Datacenter_0 *****

User id    Debt

3          35.6

CloudSimExample1 finished!
```

---

# Analysis of Simulation Output

The simulation output provides information about the execution of the Cloudlet.

| Parameter         | Description                                                    |
| ----------------- | -------------------------------------------------------------- |
| **Cloudlet ID**   | Unique identifier of the Cloudlet                              |
| **Status**        | Indicates whether the Cloudlet execution was successful        |
| **Datacenter ID** | Identifier of the Datacenter where the task was executed       |
| **VM ID**         | Identifier of the VM that executed the Cloudlet                |
| **Time**          | Total execution time                                           |
| **Start Time**    | Time at which Cloudlet execution started                       |
| **Finish Time**   | Time at which Cloudlet execution completed                     |
| **Debt**          | Resource usage/cost information associated with the cloud user |

A status of `SUCCESS` indicates that the Cloudlet was successfully executed.

---

## Important CloudSim Components

### 1. Datacenter

Represents the cloud infrastructure and provides physical computing resources.

### 2. Host

Represents a physical machine inside the Datacenter.

### 3. Virtual Machine

Represents a virtualized computing environment running on a physical host.

### 4. DatacenterBroker

Acts as an intermediary between the cloud user and the Datacenter.

### 5. Cloudlet

Represents a task or workload submitted by the user.

### 6. VM Allocation Policy

Determines how VMs are allocated to physical hosts.

### 7. Cloudlet Scheduler

Determines how Cloudlets are scheduled for execution within a VM.

---

## Result

A cloud computing scenario was successfully simulated using the CloudSim toolkit in Eclipse IDE.

Datacenters, Hosts, VMs, DatacenterBroker, and Cloudlets were created and configured. The Cloudlets were submitted to the virtual machines and successfully executed during the simulation.

The simulation output was analyzed using parameters such as execution status, start time, finish time, VM ID, Datacenter ID, and resource usage.

---

## Conclusion

This experiment demonstrated how CloudSim can be configured and used in Eclipse IDE to model a cloud computing environment.

The experiment provided practical understanding of Datacenters, Hosts, Virtual Machines, Brokers, Cloudlets, VM allocation, and Cloudlet scheduling. A custom scheduling approach can also be implemented and evaluated using the CloudSim simulation environment without requiring physical cloud infrastructure.
