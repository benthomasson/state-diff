
from deepdiff import DeepDiff

from .rule import select_rules_recursive, deduplicate_rules


def desired_state_diff(current_desired_state, new_desired_state, rules):
    '''
    desired_state_diff creates playbooks and runs them with ansible-runner to
    implement the differences between two version of state:
    current_desired_state and new_desired_state.
    '''

    # Find the difference between states

    diff = DeepDiff(current_desired_state,
                    new_desired_state, ignore_order=True)
    # Find matching rules

    matching_rules = select_rules_recursive(
        diff, rules['rules'], current_desired_state, new_desired_state)

    dedup_matching_rules = deduplicate_rules(matching_rules)

    return dedup_matching_rules
