# Install Work Governor

This is a Codex repository marketplace. It installs one plugin containing four skills and seven supporting references.

## Requirements

- A Codex installation with plugin and repository-marketplace support, with its normal account/setup completed.
- The `codex` command available in your terminal. Git-backed marketplace setup also needs Git and access to GitHub.
- Permission to add plugins in your environment. Organization policies can restrict available sources.

The GitHub marketplace and plugin installation commands below were successfully executed with Codex CLI 0.153.4 on macOS on 7 September 2026, using separate state with access to the author's personal configuration and plugins denied. A fresh installation of 0.1.1 and an update from 0.1.0 both passed. A fresh app-server discovered all four skills from 0.1.1 without errors. CLI 0.146.0 was inspected for command support only. This is not a minimum-version claim or a Desktop behavior test. Check your installed client's `codex plugin --help` if a command is unavailable; do not edit personal configuration manually to work around unsupported features.

## Public repository route

**Public preview; isolated CLI installation passed.** The repository `skiriks/work-governor` is public. Anonymous download, installation, and skill discovery were verified on 7 September 2026. A fresh native task on the author's Desktop profile completed the demo file workflow; public-plugin invocation, native-card rendering, and answer handling were also checked in that profile. Independent-profile behavior remains unverified. Use the following marketplace route in a Codex version that supports it.

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

## Update an existing public installation

Refresh only this marketplace, then reinstall the plugin from its updated snapshot:

```bash
codex plugin marketplace upgrade skiriks-work-governor
codex plugin add work-governor@skiriks-work-governor
codex plugin list
```

This update path was tested from 0.1.0 to 0.1.1. Start a new Codex task after updating; the existing task may retain earlier instructions.

On 8 September 2026, the same route updated the author's sole public Work Governor installation from 0.1.2 to 0.1.3. All 20 installed files matched the published plugin, and a fresh Codex process discovered four enabled skills without errors. This verifies the update and discovery, not new Desktop model behavior.

For the icon release, a fresh 0.1.2 installation passed in isolated CLI state. An update from 0.1.1 to 0.1.2 also passed on the author's existing Desktop profile: all 20 installed files matched the public package, and the personal plugin was preserved. Codex resolved the icon metadata in the isolated check; visible icon rendering in the Desktop UI remains unconfirmed.

## Local checkout route

If you already have the complete repository folder, open a terminal in its root:

```bash
python3 scripts/check_package.py
codex plugin marketplace add .
codex plugin add work-governor@skiriks-work-governor
codex plugin list
```

The check needs Python 3.9 or newer; plugin runtime instructions do not. These installation steps deliberately change your own Codex plugin configuration. The GitHub route above was tested in isolated CLI state; this local-checkout variant was not separately executed.

Keep the repository structure intact: `.agents/plugins/marketplace.json` resolves `./plugins/work-governor` from the **repository root**, not from the `.agents/plugins` directory. Do not copy the four skills separately.

## Verify the installation and start

1. Confirm **Work Governor** is installed and enabled from **Skiriks Work Governor**, at the published version `0.1.3`.
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
