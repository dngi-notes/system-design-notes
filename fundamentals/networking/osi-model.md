# The OSI Model

### Purpose
The purpose of the Open Systems Interconnection **(OSI)** model is to provide a standard for people developing interconnected systems.

### How it works
- The OSI model is abstracted into seven layers in increasing closeness to the end user (`i.e. 7:closest, 1:furthest`)
- Each layer has its own **Protocol Data Unit (PDU)** - the specific name for the data format at that layer:

| Number| Layer  | PDU | Function | 
| ----| ------------ | ---------- | ---------------------------------------------------------------------------------------- |
| 7   | Application  | Data | High level protocols such as resource sharing/remote file access e.g. HTTP, gRPC         |
| 6   | Presentation | Data | Translation of data between a networking service and an application; including character encoding, data compression and encryption/decryption         |
| 5   | Session      | Data | Managing communication sessions i.e. continuous information exchange in the form of multiple back-and-forth transmissions between two nodes          |
| 4   | Transport    | Segment/Datagram | Transmission of data segments between points on a network, including segmentation, acknowledgement, and multiplexing **TCP vs UDP**         |
| 3   | Network      | Packet | Structuring and managing a multi-node network, including addressing (**IP**), routing, traffic control |
| 2   | Data Link    | Frame | Transmission of data frames between two nodes connected by a physical layer e.g. **ethernet, wi-fi**|
| 1   | Physical     | Bit | Transmission and reception of raw bit streams over a physical medium          |
