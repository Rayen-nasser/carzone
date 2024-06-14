# your_app/fields.py

from multiselectfield import MultiSelectField

class CustomMultiSelectField(MultiSelectField):
    def _get_flatchoices(self):
        # Create a flat list of choices if not already cached
        if not hasattr(self, '_flat_choices_cache'):
            self._flat_choices_cache = list(self.choices)
        return self._flat_choices_cache

    @property
    def flatchoices(self):
        return self._get_flatchoices()
