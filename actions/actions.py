from typing import Text, Any, Dict

from rasa_sdk import FormValidationAction, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

from .slot import PizzaSize, PizzaCrust, PizzaTopping

pizza_sizes = [m.value for m in PizzaSize]
pizza_crusts = [m.value for m in PizzaCrust]
pizza_toppings = [m.value for m in PizzaTopping]


class PizzaFormValidator(FormValidationAction):
    def name(self) -> Text:
        return 'validate_pizza_form'

    def validate_pizza_size(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        print(slot_value)
        slot_name = 'pizza_size'
        if slot_value not in pizza_sizes:
            dispatcher.utter_message(f'We only serve: {"/".join(pizza_sizes)} pizzas. '
                                     f'Please, specify one of the above.')
            return {slot_name: None}
        return {slot_name: slot_value}

    def validate_pizza_crust(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        slot_name = 'pizza_crust'
        if slot_value not in pizza_crusts:
            dispatcher.utter_message(f'We only serve: {"/".join(pizza_crusts)} crusts. '
                                     f'Please, specify one of the above.')
            return {slot_name: None}
        return {slot_name: slot_value}

    def validate_pizza_toppings(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict
    ) -> Dict[Text, Any]:
        slot_name = 'pizza_toppings'
        if slot_value not in pizza_toppings:
            dispatcher.utter_message(f'We only serve: {"/".join(pizza_toppings)} toppings. '
                                     f'Please, specify one of the above.')
            return {slot_name: None}
        return {slot_name: slot_value}
