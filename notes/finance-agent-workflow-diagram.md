# Agentic Workflow Map

## 1. User Question 
EX: Why did operating margin decline?

## 2. Agent Instructions 
- Use approved sources
- Cite evidence
- Separate facts from interpretation
- Do not make an investment recommendation

## 3. Approved Sources / Tools
- 10-K or 10-Q
- Earnings release
- SEC company facts
- Python financial-calculation tool

## 4. Retrieval and Calculation 
- Find Revenue and operating-income data
- Retrieve management's explanation
- Calculate operating margin by period

## 5. Structured Answer 
- Financial Results
- Margin calculation
- Source evidence
- Possible explanation
- Limitations / unanswered questions

## 6. Human Review
- Check calculations and sources
- Judge whether the explanation is reasonable
- Make the final finance decision

# Completed Basic Finance-agent workflow.

```mermaid 
flowchart TD
  A[User Question:<br/>Why did operating margin decline?]
  B[Agent Instructions:<br/>Use approved sources<br/>Cite evidence<br/>Separate facts from interpretation<br/>No investment recommendation]
  C[Approved Sources and Tools:<br/>10-K / 10-Q<br/>Earnings release<br/>SEC company facts<br/>Python calculation tool]
    D[Retrieval and Calculation:<br/>Find revenue and operating income<br/>Retrieve management explanation<br/>Calculate operating margin]
    E[Structured Answer:<br/>Financial results<br/>Margin calculation<br/>Source evidence<br/>Limitations]
    F[Human Review:<br/>Check sources and calculations<br/>Assess conclusion<br/>Make final decision]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
```
