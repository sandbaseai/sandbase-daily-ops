# SandBase Daily Ops

Daily operating system for SandBase product launches, content distribution, and community updates.

This repo keeps reusable skills, playbooks, templates, scripts, and example outputs for shipping SandBase updates consistently across:

- Blog
- LinkedIn
- X / Twitter
- Discord
- Medium
- Zhihu

More channels can be added later (DEV Community, Xiaohongshu, WeChat Channels), but the
first version stays focused on company-facing global distribution plus Chinese long-form.

## Structure

```text
skills/
  api-launch-publish/        # API / provider / Agent Service launch workflow
playbooks/
  api-launch-sop.md          # Human-readable launch checklist
outputs/
  exa-search-launch/         # First example: Exa Search on SandBase.ai
```

## First Skill

`skills/api-launch-publish` turns a rough API description into a standard launch package:

```text
API name + description
  -> positioning
  -> 3 blog drafts (owned launch / comparison / 2026 Top N), EN + ZH
  -> LinkedIn copy
  -> X copy
  -> Discord announcement
  -> Medium argument
  -> Zhihu question-led answer
  -> SandBase API generated launch images
```

Images are generated through SandBase API with:

```json
{
  "model": "openai/gpt-image-2",
  "output_format": "png",
  "quality": "high"
}
```

## Usage

Create or edit a launch config:

```text
skills/api-launch-publish/references/example-api-launch.json
```

Preview prompts:

```bash
python skills/api-launch-publish/scripts/generate_api_launch_images.py \
  --config skills/api-launch-publish/references/example-api-launch.json \
  --formats 16x9 4x5 \
  --print-prompts
```

Generate images:

```bash
SANDBASE_API_KEY=... python skills/api-launch-publish/scripts/generate_api_launch_images.py \
  --config skills/api-launch-publish/references/example-api-launch.json \
  --out-dir outputs/exa-search-launch \
  --formats 16x9 4x5
```

## Example

First launch example:

- `Exa Search on SandBase.ai`
- From semantic web search to reusable Agent Services
- Outputs: `outputs/exa-search-launch/`
