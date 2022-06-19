import numpy as np


class DanceStep:
    # Position Modifiers = Rotate Degree, Flip Axis (y, x), flip
    def __init__(self, identity, subidentites, frame_counts, position_modifiers, position_facing_modifier):
        pass

    def return_positional_change_and_rotational_change(self):
        pass


class Dancer:
    position_range = 3
    dancer_idxs = {'l1': 0, 'f1': 1, 'l2': 2, 'f2': 3}

    def __init__(self, identity: str, becket: bool):
        # F1 L1 0 x 1 (0, 0), (0, 1), (0, 2)
        # Empty x x x (1, 0), (1, 1), (1, 2)
        # L2 F2 2 x 3 (2, 0), (2, 1), (2, 2)
        # In beckett, set to pos 0, 2
        # Else set to pos 1, 0
        self.identity = identity
        self.role = None
        self.color_bgr = None
        self.facing_angle, self.facing_position = None, None
        self.position_yx, self.position_partner_yx, self.position_neighbor_trans_yx, self.position_neighbor_same_yx = None, None, None, None
        self.hand_engaged = None
        self.set_starting_position(becket=becket)

    def set_starting_position(self, becket):

        # Becket
        # F1 L1 0 x 1 (0, 0), (0, 1), (0, 2)
        # Empty x x x (1, 0), (1, 1), (1, 2)
        # Empty 2 x 3 (2 ,0), (2, 1), (2, 2)
        # L2 F2       (3, 0), (3, 1), (3, 2)

        # Standard
        # L1 F2 0 x 1 (0, 0), (0, 1), (0, 2)
        # Empty x x x (1, 0), (1, 1), (1, 2)
        # Empty x x x (2 ,0), (2, 1), (2, 2)
        # F1 L2 2 x 3 (3, 0), (3, 1), (3, 2)

        if self.identity == 'l1':
            if becket:
                self.position_yx = (0, 2)
            else:
                self.position_yx = (0, 0)
            self.color_bgr, self.role = np.array([255, 0, 0], dtype=np.uint8), 'lead'

        elif self.identity == 'l2':
            if becket:
                self.position_yx = (3, 0)
            else:
                self.position_yx = (3, 2)
            self.color_bgr, self.role = np.array([0, 0, 255], dtype=np.uint8), 'lead'
        elif self.identity == 'f1':
            if becket:
                self.position_yx = (0, 0)
            else:
                self.position_yx = (3, 0)
            self.color_bgr, self.role = np.array([255, 0, 0], dtype=np.uint8), 'follow'
        elif self.identity == 'f2':
            if becket:
                self.position_yx = (3, 2)
            else:
                self.position_yx = (0, 2)
            self.color_bgr, self.role = np.array([0, 0, 255], dtype=np.uint8), 'follow'

    def set_starting_facing_position(self, dancers_tuple):
        if self.identity == 'l1':
            self.facing_position = dancers_tuple[self.dancer_idxs['f2']].position_yx
        elif self.identity == 'l2':
            self.facing_position = dancers_tuple[self.dancer_idxs['f1']].position_yx
        elif self.identity == 'f1':
            self.facing_position = dancers_tuple[self.dancer_idxs['l2']].position_yx
        elif self.identity == 'f2':
            self.facing_position = dancers_tuple[self.dancer_idxs['l1']].position_yx

    def return_facing_angle(self, facing_point_yx):
        angle = np.arctan2(-(facing_point_yx[0] - self.position_yx[0]), facing_point_yx[1] - self.position_yx[1]) * 180 / np.pi
        return angle


def return_all_possible_move_table():
    def allemande(hand, subgenre, count, neighbor, same_role, current_positions, current_angles):
        if neighbor:
            if same_role:
                center_point =
                pass
            else:
                pass
        else:
            center_points = None
        if hand == 'l':
            pass
        elif hand == 'r':
            pass
    allemande_permutations, counts, requirements = ['left - half, left - one, left - one and a half,'
                                                    'right - half, right - one, right -one and a half '], [4, 8, 8], 0
    allemande_chained_permutations, counts, requirements = ['left - double, left - triple']

    pass


def return_starting_position_arrays(becket=False):
    # Starting positions are on 7 7x8 grids, with the focus set followed in the 4th grid (3 neighboring grids on each side).
    # Each 7x8 grid consists of a hands four
    # The following generates all starting positions, with their starting points they are facing (relative to their current position).
    # x_position_array (unique values) = np.ndarray([0,
    lead, follow = 1, 2
    grid_size_y_x = (8, 8)
    grid_count = 13
    grid_max_y_x = grid_size_y_x[0], grid_size_y_x[1] * grid_count
    rang_1, rang_2 = np.arange(5, grid_max_y_x[1], 10), np.arange(1, grid_max_y_x[1], 10)
    if becket:
        all_positions_lf_1_lf_2 = np.column_stack((np.arange(5, grid_max_y_x[1], 8),
                                                    np.arange(1, grid_max_y_x[1], 8),
                                                    np.arange(1, grid_max_y_x[1], 8),
                                                    np.arange(5, grid_max_y_x[1], 8))).astype(np.int16)
        positions_y = np.array([1, 1, 5, 5], dtype=np.uint8)
        facing_point_from_yx_offset = np.array([[1, 0], [1, 0], [-1, 0], [-1, 0]], dtype=np.int8)
    else:
        all_positions_lf_1_lf_2 = np.column_stack((np.arange(1, grid_max_y_x[1], 8),
                                                    np.arange(1, grid_max_y_x[1], 8),
                                                    np.arange(5, grid_max_y_x[1], 8),
                                                    np.arange(5, grid_max_y_x[1], 8))).astype(np.int16)
        positions_y = np.array([1, 5, 5, 1], dtype=np.uint8)
        facing_point_from_yx_offset = np.array([[0, 1], [0, 1], [-1, 0], [-1, 0]], dtype=np.int8)

    return all_positions_lf_1_lf_2, positions_y, facing_point_from_yx_offset

    dancers = tuple([Dancer(position, becket) for position in Dancer.dancer_idxs])
    for dancer in dancers:
        dancer.set_starting_facing_position(dancers)
    return dancers



if __name__ == '__main__':
    positions_x_l1f1_l2f2, position_y_l1f1_l2f2, facing_point_yx = return_starting_position_arrays(becket=True)
    print('b')
    pass
