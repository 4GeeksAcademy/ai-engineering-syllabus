# Platform – Asynchronous Processing

<!-- hide -->

By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors) at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![4Geeks Academy](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=x)](https://x.com/4geeksacademy)

_Estas instrucciones están [disponibles en español](./README.es.md)._

<!-- endhide -->

---

## 🎯 The Challenge

> 📌 You are building on **your own fork** of the company's **[monorepo](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo)** — not on a new repository.

Your CTO opens a **ticket** after an external provider (a notification gateway, a third-party service, whatever your system already integrates with) went down for a few minutes. During that time, several operations that depended on that provider simply failed and were lost — nobody found out until a customer asked why they never received a confirmation.

> *"I can't keep having operations that depend on an external service run inside the same request-response cycle as the user. If that service is slow or fails, I want the operation to retry on its own, without getting lost and without the user noticing anything. And if after several attempts it's still failing, I want to know — I don't want it to disappear silently."*
>
> — CTO

Three requirements from the brief define the project:

1. **Outside the request-response cycle.** The operation gets queued and a worker processes it independently — the user shouldn't have to wait for the external provider to respond in order to get their confirmation.
2. **Retries with backoff, not blind retries.** Retrying immediately and without limit can make an external outage worse. The system should wait progressively longer between attempts.
3. **Nothing disappears silently.** An operation that ultimately fails after several attempts must end up somewhere visible (a dead-letter queue), not simply vanish from the system.

### Complementary knowledge: idempotency, the problem nobody sees until it's too late

When an operation is retried automatically, there's a silent risk: the previous attempt may have actually succeeded on the external provider's side, but the confirmation never arrived in time — and the system, not knowing that, retries and executes the same operation twice. If that operation is "send a notification," the result is annoying. If it's "charge a customer" or "deduct inventory," the result is an incident. Idempotency is the property that prevents this: designing the operation so that executing it twice with the same key produces the same result as executing it once, typically through a unique idempotency key per operation that the system checks before processing.

---

## 🌱 How to Start the Project

1. `pull` the latest changes from your fork of the monorepo.
2. Identify which operations in your current system depend on external services and currently run synchronously inside the request-response cycle.
3. Create a new branch: `feature/async-processing`.
4. Pick one concrete candidate operation from your system to migrate to this pattern (you don't need to migrate all of them).
5. Design the queue message contract first (what data the worker needs to process the task independently) before writing the worker.

---

## 💻 What You Need to Do

**Queue infrastructure**

- [ ] Set up a queueing system (e.g., Redis with RQ/Celery, or the queue manager already in your stack)
- [ ] Implement at least one worker that consumes the queue independently from the main API process

**Retries and resilience**

- [ ] Implement automatic retries with exponential backoff on external service failures
- [ ] Define a maximum number of retries, after which the task is considered permanently failed
- [ ] Implement a dead-letter queue where tasks that exhausted their retries end up

**Idempotency**

- [ ] Implement an idempotency key per queued operation
- [ ] Before processing a task, verify that key hasn't already been successfully processed
- [ ] Write a test demonstrating that queueing the same operation twice with the same key doesn't produce the duplicated effect

**Minimum observability**

- [ ] Expose the status of a queued task (pending, in progress, completed, failed) in a queryable way
- [ ] Log how many retries each task went through before completing or permanently failing

---

## ✅ What We Will Evaluate

- [ ] At least one real operation in your system runs asynchronously through the queue, outside the request-response cycle
- [ ] A simulated external service failure triggers retries with backoff, verifiable in the logs or the task's status
- [ ] A task that exhausts its retries ends up in the dead-letter queue, not gone
- [ ] Queueing the same operation twice with the same idempotency key doesn't produce the duplicated effect, demonstrated with a test
- [ ] The status of any queued task is queryable

---

## 📦 How to Submit

Open a Pull Request from your `feature/async-processing` branch to `main` on your fork. In the PR description, include which operation you migrated to the async pattern and why, and evidence of the idempotency test. Request sign-off from your CTO before merging.

---

This and many other projects are built by students as part of the [Coding Bootcamps](https://4geeksacademy.com/) at 4Geeks Academy. By [@4geeksacademy](https://github.com/4geeksacademy) and [other contributors](https://github.com/4GeeksAcademy/ai-engineering-company-project-monorepo/graphs/contributors). Find out more about [Full-Stack Software Developer](https://4geeksacademy.com/en/career-programs/full-stack), [Data Science & Machine Learning](https://4geeksacademy.com/en/career-programs/data-science-ml), [Cybersecurity](https://4geeksacademy.com/en/career-programs/cybersecurity) and [AI Engineering](https://4geeksacademy.com/en/career-programs/ai-engineering).
