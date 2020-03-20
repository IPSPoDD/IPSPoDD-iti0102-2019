"""PR11 Drawing."""


class DrawingFullError(Exception):
    """DrawingFullError."""

    pass


class FigureDoesNotExistError(Exception):
    """FigureDoesNotExistError."""

    pass


class DrawingCanvas:
    """A drawing canvas where one can draw some simple figures."""

    def __init__(self, max_figures: int, author: str):
        """
        Initialize the canvas.

        You should initialize your variables (properties) here.

        :param max_figures: The maxim amount of figures on the drawing.
        :param author: The author of the drawing.
        """
        self.max_figures = max_figures
        self.author = author
        self.figures = []

    def draw_figure(self, figure: str) -> str or None:
        """
        Draw a new figure.

        If the drawing has already reached maximum amount of figures
        don't add this figure and throw a DrawingFullError with the
        message "The drawing is full".

        There can be only unique figures on the drawing.
        This means that there is no way that, for example, two or more
        circles are on the drawing.
        In this case method does nothing and returns None.

        :param figure: A figure to draw.
        :return: The newly drawn figure.
        """
        if self.size() < self.max_figures:
            if figure not in self.figures:
                self.figures.append(figure)
                return figure
        if self.size() >= self.max_figures:
            raise DrawingFullError("The drawing is full")

    def erase_figure(self, figure: str) -> str:
        """
        Erase the figure.

        If there is no such figure throw a FigureDoesNotExistError
        with the message "There is no such figure on the drawing".

        :return: The erased figure.
        """
        if figure in self.figures:
            self.figures.remove(figure)
            return figure
        raise FigureDoesNotExistError("There is no such figure on the drawing")

    def is_empty(self) -> bool:
        """
        Find out whether the drawing is empty or not.

        Empty means there are not any figures drawn on it.

        :return: True if empty, False otherwise.
        """
        if self.size() == 0:
            return True
        return False

    def size(self) -> int:
        """Return the amount of figures on the drawing."""
        return len(self.figures)

    def __str__(self):
        """
        A string representation of the drawing.

        The returned string must follow this pattern:
        "The drawing painted by {author}. Contains {current amount of figures} figure(s)"

        :return: A correct string representing the drawing.
        """
        return f'The drawing painted by {self.author}. Contains {self.size()} figure(s)'


if __name__ == '__main__':
    dc = DrawingCanvas(5, "Person")

    print("Check attributes:")
    try:
        print(dc.max_figures)  # -> 5
        print(dc.author)  # -> Person
        print(dc.figures)  # -> Empty data structure (it depends on which one you have chose)
    except AttributeError:
        print("Not all of the required attributes are defined")
        exit()

    print()
    print("Canvas after creation:")
    print(dc.is_empty())  # -> True
    print(dc.size())  # -> 0
    print(dc.figures)  # -> Empty data structure (it depends on which one you have chose)

    print()
    print("Draw figures:")
    print(dc.draw_figure("circle"))  # -> circle
    print(dc.draw_figure("triangle"))  # -> triangle
    print(dc.draw_figure("Mona Lisa"))  # -> Mona Lisa
    print(dc.draw_figure("circle"))  # -> None

    print()
    print("After drawing:")
    print(dc.size())  # -> 3
    print(dc.is_empty())  # -> False
    print(dc.figures)  # -> Data structure containing 1 circle, 1 triangle and 1 Mona Lisa
    print(dc)  # -> The drawing painted by Person. Contains 3 figure(s)

    print()
    print("Draw figures when canvas is full:")
    try:
        dc.draw_figure("1")
        dc.draw_figure("2")
        dc.draw_figure("3")
    except DrawingFullError as e:
        print(e)  # -> The drawing is full
    else:
        print("The drawing is full, but exception wasn't thrown")
        exit()
    print(dc.size())  # -> 5
    print(dc.figures)  # -> Data structure containing circle, triangle, Mona Lisa, 1, 2

    print()
    print("Erase figures:")
    dc.erase_figure("1")
    dc.erase_figure("2")

    print(dc.erase_figure("triangle"))  # -> triangle
    print(dc.figures)  # -> Data structure containing circle and Mona Lisa
    print(dc.size())  # -> 2

    print(dc.erase_figure("Mona Lisa"))  # -> Mona Lisa
    print(dc.figures)  # -> Data structure containing only circle
    print(dc.size())  # -> 1

    print(dc.erase_figure("circle"))  # -> circle
    print(dc.figures)  # -> Empty data structure

    print()
    print("After erasing:")
    print(dc.is_empty())  # -> True
    print(dc.size())  # -> 0
    print(dc)  # -> The drawing painted by Person. Contains 0 figure(s)

    print()
    print("Erase non-existing figure:")
    try:
        dc.erase_figure("circle")
    except FigureDoesNotExistError as e:
        print(e)  # -> There is no such figure on the drawing
    else:
        print("There is no such figure, but exception wasn't thrown.")
