import arcade
import numpy as np


class Simulator(arcade.Window):
    def __init__(
        self,
        w_width: int = 800,
        w_height: int = 600,
        rows: int = 10,
        columns: int = 10,
        update_interval: float = 0.5,
    ) -> None:
        super().__init__(width=w_width, height=w_height, title='Simulation')

        arcade.set_background_color(arcade.color.BLACK)

        self.rows = rows
        self.columns = columns
        self.grid = np.zeros((self.rows, self.columns))
        self.grid = np.where(np.random.rand(self.rows, self.columns) < 0.5, 1, 0)

        self.gap = 5
        self.c_w = (w_width - (self.columns + 1) * self.gap) / self.columns
        self.c_h = (w_height - (self.rows + 1) * self.gap) / self.rows

        self.time = 0
        self.update_interval = update_interval

    def setup(self) -> None:
        pass

    def on_draw(self) -> None:
        arcade.start_render()

        for row in range(self.rows):
            for column in range(self.columns):
                if self.grid[row, column] == 1:
                    color = arcade.color.GREEN_YELLOW
                else:
                    color = arcade.color.GRAY

                x = (self.gap + self.c_w) * column + self.gap + self.c_w // 2
                y = (self.gap + self.c_h) * row + self.gap + self.c_h // 2

                arcade.draw_rectangle_filled(x, y, self.c_w, self.c_h, color)

    def on_update(self, delta_time) -> None:
        self.time += delta_time
        if self.time > self.update_interval:
            self.time = 0
            self.grid = np.where(np.random.rand(self.rows, self.columns) < 0.5, 1, 0)

    def on_key_press(self, key, key_modifiers) -> None:
        pass

    def on_key_release(self, key, key_modifiers) -> None:
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y) -> None:
        pass

    def on_mouse_press(self, x, y, button, key_modifiers) -> None:
        pass

    def on_mouse_release(self, x, y, button, key_modifiers) -> None:
        pass


def main():
    engine = Simulator()
    engine.setup()
    arcade.run()


if __name__ == "__main__":
    main()
