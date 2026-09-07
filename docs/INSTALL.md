# Install Work Governor

This is a Codex repository marketplace. It installs one plugin containing four skills and seven supporting references.

## Requirements

- A Codex installation with plugin and repository-marketplace support, with its normal account/setup completed.
- The `codex` command available in your terminal. Git-backed marketplace setup also needs Git and access to GitHub.
- Permission to add plugins in your environment. Organization policies can restrict available sources.

Authoring command support was inspected in Codex CLI 0.146.0 and the bundled 0.153.4 on 7 September 2026. This is not a minimum-version claim or evidence of a successful public install. Check your installed client's `codex plugin --help` if a command is unavailable; do not edit personal configuration manually to work around unsupported features.

## Public repository route

**Pending publication and remote installation verification.** The following is the planned route for `skiriks/work-governor`; it cannot succeed until that repository is public and contains this reviewed package.

```bash
codex plugin marketplace add skiriks/work-governor
codex plugin marketplace list
```

Confirm the marketplace identity is `skiriks-work-governor`. Its display title is **Skiriks Work Governor**.

In the Codex desktop plugin directory, choose that marketplace/source, open **Work Governor**, and install/enable it. Restart the app if the newly added source has not appeared. Surface availability varies; the command adding a marketplace alone does not prove the plugin is installed.

The inspected CLI also exposes this explicit installation command:

```bash
codex plugin add work-governor@skiriks-work-governor
codex plugin list
```

Use either the supported desktop install flow or the CLI flow available in your version. Verify the result rather than assuming command delivery means success.

## Local candidate route

If you have the complete repository folder before publication, open a terminal in its root:

```bash
python3 scripts/check_package.py
codex plugin marketplace add .
codex plugin add work-governor@skiriks-work-governor
codex plugin list
```

The check needs Python 3.9 or newer; plugin runtime instructions do not. These installation steps deliberately change your own Codex plugin configuration. They were prepared for the candidate but have not been run in an independent environment.

Keep the repository structure intact: `.agents/plugins/marketplace.json` resolves `./plugins/work-governor` from the **repository root**, not from the `.agents/plugins` directory. Do not copy the four skills separately.

## Verify the installation and start

1. Confirm **Work Governor** is installed and enabled from **Skiriks Work Governor**, version `0.1.0`.
2. In Codex's available skills, confirm `work-governor`, `research`, `writing-for-agents`, and `chat-management`. The host may display these with the `work-governor:` namespace.
3. Start a new task in an empty demo folder. In the `@` picker, select **Work Governor from this marketplace**. Do not reuse a mention copied from another person's personal installation.
4. Follow [the offline demo](../examples/OFFLINE-DEMO.md). Confirm that Codex reads and applies the packaged instructions, creates the requested artifact only after authorization, and checks it against the supplied brief.
5. Run the missing-capability cases and record what actually happened.

If an older installation with the same display name is present, identify the marketplace before selecting. Do not remove your working version just to try this candidate. An isolated test account/profile or separate machine gives better evidence of a clean install.

## If something is missing

- **Marketplace absent:** inspect `codex plugin marketplace list`, GitHub access, and your host's support for repository sources. Restart the app if required by your version.
- **Plugin absent:** confirm the complete repository tree and correct source path; adding a catalog does not install its entries automatically.
- **Skill absent:** confirm the plugin is enabled and the installation contains all four folders under `skills/`. Start a new task after installation.
- **No `@` picker support:** a plain-language request can exercise instructions where the host exposes the skill, but does not establish that the Desktop mention route works.
- **Question cards or task tools unavailable:** use the host-permitted clarification or continuation path. Treat that capability as unverified; do not claim the plugin supplies its own UI or task engine.

The [official packaging guide](https://developers.openai.com/plugins/build/plugins) documents repository sources. Listing in the [official public directory](https://developers.openai.com/plugins/deploy/submission) is a separate reviewed publication route.
