# Lab 01 – Lab Setup (1 of 2): Virtualization
### Private Tutor Guide — One Step at a Time

> **How to use this guide:**
> Work through each step in order. Do **not** skip ahead — fully complete each step before moving to the next one.
> Every step includes:
> - **How to do it** — clear, technical, hands-on instructions.
> - **What is its purpose?** — the goal of the step and why it matters in the context of this lab.

---

## Step 1 — Install VMware Workstation for Windows

### How to do it

1. Locate the installer file named `VMware-workstation-full-17.5.2-xxxxxx-Win.exe` (provided locally or in the shared location specified by your instructor).
2. Double-click the `.exe` file to start the installation wizard.
3. Follow the on-screen prompts, keeping all settings at their **default values**.
4. When prompted, grant permission to install the required **device drivers** (e.g., virtual network adapters).
5. Wait for the installation to complete, then click **Finish**.

### What is its purpose?

VMware Workstation is a **Type-2 hypervisor** — software that runs on top of your existing Windows operating system and lets you create and run isolated virtual machines (VMs). Installing it is the mandatory first step because every subsequent task in this lab depends on having a working hypervisor. Using the default settings ensures compatibility with later labs in the course.

> ⚠️ **Note:** No hypervisor other than VMware is accepted for this course — using VirtualBox or Hyper-V will cause compatibility problems in future labs.

---

## Step 2 — Launch VMware Workstation

### How to do it

1. After installation, find the **VMware Workstation** shortcut on your desktop, or search for it in the **Start Menu**.
2. Double-click the shortcut to open the application.
3. Accept any license agreement prompt if it appears on first launch.
4. Confirm that the main VMware Workstation window opens without errors.

### What is its purpose?

Launching VMware Workstation verifies that the installation completed successfully and that the application is ready for use. The main window is where you will manage all virtual machines — creating, running, pausing, and deleting them. Opening it here confirms your environment is correctly set up before you begin creating a VM.

---

## Step 3 — Create a New Virtual Machine

### How to do it

1. In VMware Workstation, click **File → New Virtual Machine…** (or press `Ctrl+N`).
2. When the wizard opens, select **Typical (recommended)** and click **Next**.
3. On the "Guest Operating System Installation" screen, select **Installer disc image file (iso)** and browse to the Kali Linux ISO file provided by your instructor (`kali-linux-2024.4-installer-amd64.iso`).
4. Click **Next** through the wizard. When you reach hardware configuration options, set the following specifications:
   - **Number of processors (vCPUs):** 2
   - **Memory (RAM):** 8192 MB (8 GB)
   - **Hard Disk (HDD) size:** 60 GB
5. Complete the wizard and click **Finish** to create the VM.

### What is its purpose?

This step creates the virtual machine — a software-defined computer that runs inside your physical PC. Allocating **2 vCPUs** ensures the VM has enough processing power for security tools. **8 GB of RAM** gives Kali Linux adequate memory to run smoothly. **60 GB of disk** provides enough storage for the OS and the tools you will install throughout the course.

---

## Step 4 — Install Kali Linux and Configure Disk Partitions

### How to do it

1. Start the VM you just created. The Kali Linux installer will boot automatically from the ISO.
2. Follow the Kali installer prompts until you reach the **Partition Disks** screen.
3. Choose **Manual** partitioning and configure the following layout on the 60 GB virtual disk:
   - **Root partition `/`** — Size: **48 GB**, Filesystem: **ext4**, Mount point: `/`
   - **Swap partition** — Size: **12 GB**, Type: **swap**
4. Confirm and apply the partition configuration to proceed with the installation.

### What is its purpose?

Partitioning the disk correctly ensures the operating system has dedicated space for all its files and for virtual memory (swap). The **root `/` partition (ext4)** is where Kali Linux and all installed applications will reside. The **swap partition** acts as an overflow area for RAM — when RAM is fully used, Linux temporarily stores inactive data here, preventing crashes. Using the manual layout gives you full control and teaches fundamental Linux disk management.

---

## Step 5 — Set Hostname and Username During Installation

### How to do it

1. During the Kali Linux installation, when prompted for a **hostname**, enter:
   ```
   Student<Your-AIU-ID>
   ```
   *(Replace `<Your-AIU-ID>` with your actual student ID number, e.g., `Student12345`.)*

2. When prompted for a **username**, enter your name using the format:
   ```
   <first name initial><last name>
   ```
   *(For example, if your name is John Smith, enter: `jsmith`.)*

3. Set a secure password for this user account when prompted.

### What is its purpose?

The **hostname** uniquely identifies your virtual machine on the network and in lab reports — your instructor uses it to verify your work. The **username** follows a naming convention that makes it easy to identify who owns the VM. Establishing these identifiers now ensures all screenshots and outputs throughout the course clearly show the correct machine and user.

---

## Step 6 — Update and Upgrade Kali Linux, Then Reboot

### How to do it

1. After the Kali installation finishes and the VM boots to the desktop, open a **Terminal** window.
2. Run the following commands one at a time:
   ```bash
   sudo apt update
   sudo apt upgrade -y
   ```
3. Wait for both commands to complete (this may take several minutes depending on your internet connection).
4. Reboot the VM to apply all updates:
   ```bash
   sudo reboot
   ```
5. After the VM restarts, log in and confirm it boots and logs in normally.

### What is its purpose?

`apt update` refreshes the list of available packages from Kali's repositories — it does **not** install anything, it just downloads the latest package index. `apt upgrade` then installs the newest versions of all currently installed packages. This step is critical because a fresh Kali installation may have outdated software with known **security vulnerabilities**. Keeping the OS up to date is a fundamental security practice and ensures your tools work correctly.

---

## Step 7 — Install VMware Tools (Guest Tools)

### How to do it

1. Boot the VM and open a **Terminal** window.
2. Log in as (or switch to) the **root** user, then run the following commands:
   ```bash
   sudo apt update
   sudo apt install -y --reinstall open-vm-tools-desktop
   sudo reboot -f
   ```
3. Wait for the VM to restart. After it reboots, log back in and verify the installation completed without errors.

### What is its purpose?

**VMware Tools** (also called "Guest Tools") is a package of drivers and utilities installed *inside* the guest OS to improve how the VM interacts with the host. Without it, the VM window may not resize properly, copy-paste between host and guest won't work, and mouse integration may be poor. Installing `open-vm-tools-desktop` — the open-source version provided by Kali's package manager — is the recommended method because it integrates cleanly with the system and updates automatically alongside other packages.

---

## Step 8 — Add Support for Shared Folders

### How to do it

1. After the reboot, open a **Terminal** window.
2. Run the Kali tweaks configuration tool:
   ```bash
   kali-tweaks
   ```
3. In the Kali Tweaks menu, navigate to **Virtualization**.
4. Select **"Install additional packages and scripts for VMware"**.
5. Follow the on-screen instructions to complete the installation of the shared folder support packages.

### What is its purpose?

Shared folder support allows you to access folders from your **host (Windows) PC** directly inside the **guest (Kali Linux) VM**. This is essential for moving files — such as lab materials, scripts, or screenshots — between the two systems without needing a USB drive or network transfer. `kali-tweaks` is a purpose-built tool in Kali that simplifies the configuration of common virtualization enhancements.

---

## Step 9 — Configure and Mount a Shared Folder

### How to do it

1. In VMware Workstation (on your host), right-click your VM and go to **Settings → Options → Shared Folders**.
2. Enable shared folders and add the host folder you want to share (e.g., `C:\Users\YourName\Desktop\SharedFiles`).
3. Inside the Kali VM, open a Terminal and run:
   ```bash
   sudo mount-shared-folders
   ```
4. The shared folder will be mounted and accessible from within the VM.
5. Test the setup by creating or copying a file on the host side and verifying it appears inside the VM, and vice versa.

### What is its purpose?

This step brings the shared folder configuration to life by **mounting** the host directory so Linux can read and write to it. Mounting is how Linux makes storage devices and network shares accessible — you assign them a location in the filesystem. Testing the file transfer confirms the guest tools are working correctly and that you have a reliable channel for moving data between host and guest throughout all future labs.

---

## Step 10 — Shut Down the VM and Create a Snapshot

### How to do it

1. Gracefully shut down the Kali VM:
   ```bash
   sudo shutdown -h now
   ```
2. Once the VM is powered off, go to VMware Workstation's **VM** menu and click **Snapshot → Take Snapshot…**
3. Name the snapshot using the same name as your guest VM (the hostname you set in Step 5), postfixed with `-snapshot-1`. For example:
   ```
   Student12345-snapshot-1
   ```
4. Optionally, add a short description (e.g., "Fresh Kali install with VMware Tools") and click **Take Snapshot**.

### What is its purpose?

A **VM snapshot** saves the exact state of your virtual machine at a specific point in time — including the disk, memory, and settings. If anything goes wrong in a future lab (a misconfiguration, a corrupted file, an accidental deletion), you can **revert to this snapshot** and instantly restore the VM to this clean, working state. Creating a snapshot after the initial setup is a best practice in any lab or development environment, acting as a guaranteed restore point before any risky operations begin.

---

## Summary of All Steps

| Step | Task | Section |
|------|------|---------|
| 1 | Install VMware Workstation | 1.1 |
| 2 | Launch VMware Workstation | 1.1 |
| 3 | Create a New Virtual Machine | 1.2 |
| 4 | Install Kali Linux and configure disk partitions | 1.2 |
| 5 | Set hostname and username | 1.2 |
| 6 | Update and upgrade Kali Linux, then reboot | 1.2 |
| 7 | Install VMware Tools (Guest Tools) | 1.3 |
| 8 | Add support for shared folders | 1.3 |
| 9 | Configure and mount a shared folder | 1.3 |
| 10 | Shut down the VM and create a snapshot | 1.3 |

---

*This guide is based on **Lab 01 — Lab Setup (1 of 2): Virtualization** for CSE241, Spring 2026, taught by Dr. Islam Moursy.*
