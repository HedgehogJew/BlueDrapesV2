model.eval1()

print(evaluate(
    model,
    char_to_idx,
    idx_to_char,
    temp=0.3,
    prediction_len=1000,
    start_text='тварь '
    )
)