# Logic prototype

Prefer one self-contained offline HTML file for a question about state, transitions, or data shape. Keep the model pure and the surrounding page a thin disposable driver.

## Artifact

- State the design question visibly at the top.
- Represent state in readable domain terms. Render the full relevant state after every action and call out the last change when helpful.
- Put logic in one DOM-independent module: a reducer, explicit state machine, or small set of pure functions chosen for the question.
- Provide free-play controls for every relevant action.
- Provide repeatable guided walkthroughs that reset to a known state. Cover the ordinary path, the agreed awkward edge, and an illegal or rejected action when relevant.
- Use one file with inline HTML, CSS, and JavaScript so it can open without a server, framework, dependency, or network.

Use only the authorized path and synthetic inputs. Exercise the agreed cases and confirm the artifact remains offline and runnable. Add targeted checks when the prototype's risk or host rules require them; a blanket test ban is not part of prototyping.

Record what the walkthrough demonstrated and what remains unknown. The pure module may inform later work, but lifting it into production requires separately authorized implementation and production evidence.
