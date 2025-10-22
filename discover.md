```mermaid
      flowchart TD
    A[Tourist Opens Website] --> B{Is User Logged In?}
    B -- No --> C[Sign Up / Login]
    B -- Yes --> D[Dashboard / Home Page]
    
    D --> E[Home Page]
    D --> F[Registration and Map]
    D --> G[About Us]
    D --> H[News]
    D --> I[Adventures]
    D --> J[Video Media]
    D --> K[Regional Info]
    D --> L[Tour Guide Agency]
    D --> M[Hotel Info]
    
    F --> N[Google Maps Integration]
    L --> O[Tour Guide Registration & Verification]
    M --> P[Hotel & Facility Details]
    
    C --> D
    N --> Q[Explore Destinations on Map]
    O --> R[Book Verified Guides]
    P --> S[Book Hotels / Facilities]
    
    Q --> T[Tourist Access Destination Info]
    R --> T
    S --> T
