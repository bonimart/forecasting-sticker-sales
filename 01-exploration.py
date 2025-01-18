import marimo

__generated_with = "0.10.14"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl
    import plotly.express as px
    import seaborn as sns
    return mo, pl, px, sns


@app.cell
def _(pl):
    df = pl.read_csv("data/train.csv")
    print(df.describe())
    return (df,)


@app.cell
def _(df, mo, pl, px):
    _df = df.select(pl.col("date").value_counts(sort=True)).unnest("date")
    _plot = px.scatter(
        _df, x="date", y="count"
    )
    data_count_by_day = mo.ui.plotly(_plot)
    return (data_count_by_day,)


@app.cell
def _(data_count_by_day, mo):
    mo.hstack([data_count_by_day, data_count_by_day.value])
    return


@app.cell
def _(df, pl):
    print(df.select(pl.col("country").value_counts(sort=True)).unnest("country"))
    return


@app.cell
def _(df, pl):
    print(df.select(pl.col("store").value_counts(sort=True)).unnest("store"))
    return


@app.cell
def _(df, pl):
    print(df.select(pl.col("product").value_counts(sort=True)).unnest("product"))
    return


@app.cell
def _(df, sns):
    _plot = sns.lineplot(df, x="date", y="num_sold")
    _plot
    return


if __name__ == "__main__":
    app.run()
