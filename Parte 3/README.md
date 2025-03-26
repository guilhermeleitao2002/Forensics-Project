# Arco Underground - Digital Forensics Investigation (Stage III)

## Project Overview
The final stage of the investigation focuses on analyzing network traces to uncover the source and method of document exfiltration within IST's Department of Computer Science (DEI) network.

## Objective
Conduct a comprehensive network forensic analysis to:
- Identify document transfer evidence
- Determine the responsible parties
- Establish a comprehensive timeline of events
- Understand the motivation behind the data exfiltration

## Forensic Artifacts
### Network Traces
- **trace1.pcapng**: Network trace 1
- **trace2.pcapng**: Network trace 2
- **trace3.pcapng**: Network trace 3
- **sslkeylogfile.txt**: SSL key log file for decrypting HTTPS traffic

### Network Topology
- Gateway/Router: 194.210.63.254
- Eva Rocha's Computer: 194.210.61.134
- Rodrigo Cabaço's Computer: 194.210.62.203
- Nuno Santos' Computer: 194.210.60.57

## Key Actors
- Eva Rocha (eva.rrocha@proton.me)
- Nuno Santos (nuno.santos.1970@protonmail.com)
- Rodrigo Cabaço (presidente.rodri@mail.com)
- Golias Matos (golias.matos@mail.com)

## Investigation Tasks
1. **Document Transfer Analysis**
   - Examine network traces for evidence of file transfers
   - Verify document source and authenticity
   - Trace document movement across the network

2. **Actor Identification**
   - Identify individuals involved in document transfer
   - Analyze communication patterns
   - Correlate network activities with previous findings

3. **Timeline Reconstruction**
   - Establish a comprehensive chronology of events
   - Map document exfiltration pathway
   - Reconcile timestamps across different investigation stages

4. **Motivation Assessment**
   - Analyze collected evidence
   - Develop hypotheses about the actors' motivations
   - Provide insights into the underlying purpose of the data exfiltration

## Special Considerations
- Timestamps require 14-day adjustment
- Virtual network environment with simplified topology

## Recommended Tools
- Wireshark
- Network forensics analysis tools
- SSL/TLS decryption techniques
- Timeline reconstruction software

## Investigation Principles
- Systematic network traffic analysis
- Comprehensive evidence correlation
- Detailed documentation
- Objective interpretation of digital evidence
