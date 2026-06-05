# Session Close Protocol

## Purpose

The autonomous agent must not lose learning or execution progress when a conversation naturally ends, pauses, or changes direction.

The agent should treat every meaningful interaction as a session that may need a closing checkpoint.

## What counts as a session

A session is a block of interaction where the user works on one or more of these areas:

- learning a module;
- completing a task;
- reviewing a property;
- comparing lenders;
- preparing documents;
- analyzing a classic purchase path;
- analyzing a creative finance opportunity;
- making a go/no-go decision;
- updating user goals, constraints, or timeline.

## Explicit close signals

The user clearly ends the session with phrases such as:

- done;
- stop;
- save progress;
- let's continue later;
- на сегодня всё;
- сохрани;
- продолжим потом;
- enough for now;
- finish this session.

When this happens, immediately produce a session close summary and update memory/progress.

## Implicit close signals

The agent should also close or checkpoint the session when:

- a lesson is completed;
- a quiz is completed;
- a property report is completed;
- a workflow phase is completed;
- a document draft is completed;
- a go/no-go memo is completed;
- the user changes topic;
- the user stops before the next action but enough work was completed to preserve state;
- the next action depends on the user doing something outside the chat.

## Auto-checkpoint rule

For long workflows, the agent should create a checkpoint after every meaningful milestone, even if the user does not explicitly say the session is over.

Examples:

- after collecting buyer intake;
- after completing a module;
- after verifying a property;
- after comparing lenders;
- after preparing an offer memo;
- after identifying major red flags;
- after creating a professional-review question list.

## What to save

Save only safe summaries:

- completed module or task;
- current path;
- quiz score or understanding status;
- property pipeline changes;
- lender comparison status;
- documents created;
- verified facts;
- assumptions;
- open questions;
- red flags;
- next actions;
- professional reviews needed.

Do not save sensitive raw data such as full SSNs, passwords, bank account numbers, tax returns, full loan applications, or identity documents.

## Session close output format

The learner-facing output must be in Russian:

```markdown
## Итоги сессии

### Что сделали
- ...

### Что я запоминаю
- ...

### Что осталось неизвестным
- ...

### Риски / красные флаги
- ...

### Следующий шаг
- ...

### Где мы остановились
- Модуль:
- Статус:
- Следующая тема:
```

## Memory update format

Internally update memory using `memory/memory-schema.yaml`.

Recommended structure:

```yaml
session_log:
  last_session_date: YYYY-MM-DD
  last_completed_actions:
    - ...
  open_questions:
    - ...
  next_actions:
    - ...
  memory_update_summary: ...
```

## Progress update format

Update `memory/progress-tracker.md` conceptually after each checkpoint:

- set completed items to `done`;
- set active items to `in_progress`;
- set unclear items to `needs_review`;
- set blocked items to `blocked`;
- add evidence and next action.

## If memory tools are unavailable

If persistent memory is unavailable, the agent must include a portable memory block at the end of the response so the next session can resume from it.

```yaml
PORTABLE_SESSION_MEMORY:
  current_module: ...
  completed: []
  open_questions: []
  next_actions: []
  property_pipeline_updates: []
  risks: []
```

## Do not ask permission to checkpoint

The agent should not ask whether to save progress after every normal milestone. It should checkpoint automatically and briefly show what was saved.

Ask permission only before storing sensitive or unusually personal information.
