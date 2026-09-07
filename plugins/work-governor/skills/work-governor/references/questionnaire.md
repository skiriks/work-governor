# Recipient questionnaire

Use this method only when the user explicitly asks Work Governor to prepare questions for another person. The requested questionnaire is the deliverable, not a replacement for a failed grilling card.

## Establish the send

Reuse context already supplied. Ask the user only for missing facts they can reasonably know:

- the recipient's role, expertise, and relationship to the user;
- the specific decisions or facts the user needs back.

Never ask the user to supply technical facts held by the recipient. When a remaining send preference is material, use the Governor native-card protocol within current host restrictions. An empty or delivery-only card result leaves that preference unanswered; it does not invalidate a questionnaire whose recipient and gaps are already known.

## Draft

Return a recipient-facing draft in chat by default. Create a file or send the questionnaire only under separate exact authority.

Draft from answer fields, then render:

1. Privately list the minimum answer fields required by the supplied gaps and intended decision. Name each field by what one answer will provide, such as `identifier creation location` or `identifier creation time`. Stop at those required fields rather than adding adjacent topics.
2. Render one question and one answer space per field. If the recipient could provide one field while leaving another unknown, give them separate slots. Keep alternatives together only when they are choices for one field; for example, `Which state defines Purchase: captured, settled, or another state?` expects one classification answer.
3. Order the questions by decision value. Add enough context for a recipient who was not in the conversation, and explain why a question matters only when ambiguity would otherwise produce a weak answer. Invite partial answers, uncertainty, and `I don't know`.

Example: privately map `identifier creation location` and `identifier creation time`, then render:

```markdown
### Where is the identifier created?
> 

### When is the identifier created?
> 
```

Treat undefined relationships as their own answer field. For example, ask `Is a chargeback classified as a refund or as a separate event?` instead of assuming shared meaning.

Use this shape, omitting fields the user did not supply:

```markdown
# <Title>

**Purpose:** <decision this will support>

## Context
<Short recipient-facing context>

## How to answer
Partial and unknown answers are useful; mark uncertainty instead of skipping.

## <Priority theme>

### <One independently answerable fact or decision>
> 

## Anything else?
### What else should we know before making this decision?
> 
```

Include a deadline or expected effort only when supplied, or clearly label it as a proposal rather than a commitment.

Before returning the draft, review the rendered questions against the private field list:

- Name the expected answer field for each question. Inspect conjunctions, lists, and combined dimensions such as place/time, possibility/selection, identifier/storage, or component/cap. When clauses populate different fields, split them into separate questions and slots.
- Distinguish answer alternatives from conditional policy branches. Alternatives stay in one question when the response is one classification or requested list. Conditions that can have different rules are separate fields and slots, even when written as one list.
- Map each requested gap to its required fields, then to the rendered questions. Every required field is covered once; every rendered question covers one field; unrelated fields are omitted.

Finish when that coverage pass succeeds and the draft can be answered without access to the user's private reasoning.
