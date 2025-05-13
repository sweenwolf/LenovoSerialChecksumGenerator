# Serial Checksum Generation for Legacy Lenovo Systems

This tool is designed to help **restore the original serial number** in BIOS for legacy Lenovo systems that have encountered a **corrupted BIOS**. When a blank BIOS is flashed to revive the system, the **serial number is often removed** (for privacy reasons), causing an RFID serialization checksum error. This error can result in issues such as **invalid Windows licensing**.

If you're seeing the error **"0188: Invalid RFID Serialization Information Area"** on boot, this indicates a failure in the **RFID serialization check** due to missing or corrupted serialization data. The system will often allow you to continue booting by pressing **Esc**, but it will not resolve the underlying issue with the missing serial data.

This tool generates the **serial number checksum**, allowing users to restore their original serial number and resolve these errors.

### 1. Dump Your BIOS
The BIOS image can be dumped using either:
- A **hardware programmer**, or  
- Intel’s `fpt` (Flash Programming Tool), if supported by your system.

### 2. Open the BIOS in a Hex Editor
Open the dumped BIOS file using any hex editor of your choice.

### 3. Locate the Serial Tag
Search for the string `"SER#"` — this is displayed in the **red box** in the reference image.

### 4. Reference the Image for All Locations
Here’s an image that shows all relevant locations in the BIOS, with color-coded boxes:

![BIOS Locations](https://github.com/user-attachments/assets/f7171945-7ac6-4ac4-88a9-91477a1a23d2)
*The image highlights the locations of the Serial Number, Machine ID, and Checksum in the BIOS dump.*

### 5. Run the Python Script
- Execute the provided Python script.  
- When prompted, enter your **Machine ID** (shown in the **green box**) and **Serial Number** (shown in the **yellow box**).  
- These values are typically printed on a sticker on the underside of your laptop.

### 6. Generate the Checksum
- The script will generate a **Hex value** and an **ASCII string**, which represents the **new checksum**.  
- This checksum is used to restore the correct serial number, preventing the RFID serialization checksum error.

### 7. Modify the BIOS
Once the checksum is generated, you can use it to modify the existing checksum values. This can be done by:
- Replacing the **ASCII value** (displayed in the **blue box**) in your hex editor with the new checksum, using either the **hex values** or **ASCII characters**.

### 8. Flash the Modified BIOS
Flash the modified BIOS back to your system using one of the following methods:
- **Intel’s `fpt` tool**, if supported and permitted by your system.  
- **Hardware programmer**, such as CH341A, if `fpt` is not an option.
