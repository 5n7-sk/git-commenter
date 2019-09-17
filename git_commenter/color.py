from PyInquirer import Token, style_from_dict

STYLE = style_from_dict(
    {
        Token.Answer: "#cc5454 bold",
        Token.Instruction: "",
        Token.Pointer: "#cc5454 bold",
        Token.Question: "#3498db",
        Token.QuestionMark: "#3498db bold",
        Token.Selected: "#cc5454",
        Token.Separator: "#cc5454",
    }
)
