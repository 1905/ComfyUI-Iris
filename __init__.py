"""ComfyUI-Iris: native Iris-3B (pixel-space text-to-image) support.

Importing the pack registers the model with ComfyUI's own loaders, so the standard
Load Diffusion Model / Load CLIP / Load VAE / sampler graph runs it (base and Turbo).

The one node, IrisReady, is a ready check: it is listed in /object_info only when this
module imported and register() ran, so a host can tell a working pack from a failed import.
"""
from .iris.integration import register, registered

register()


class IrisReady:
    """Reports whether Iris-3B is registered with ComfyUI's model detection."""

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {}}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("status",)
    FUNCTION = "check"
    CATEGORY = "advanced/Iris"
    DESCRIPTION = "Ready check for the Iris-3B pack: 'ok' when the model loader recognises Iris checkpoints."

    def check(self):
        return ("ok" if registered() else "Iris-3B is not registered",)


NODE_CLASS_MAPPINGS = {"IrisReady": IrisReady}
NODE_DISPLAY_NAME_MAPPINGS = {"IrisReady": "Iris Ready Check"}
