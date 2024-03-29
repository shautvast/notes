Setup for axum serving static files and a rest API, using axum
* took me a while to get right, but now it's no use anymore
* assumes static files in ./assets

```rust
use axum::body::Body;
use axum::extract::Path;
use axum::http::{header, Request, StatusCode, Uri};
use axum::response::{IntoResponse, Response};
use axum::{routing::get, Router};
use spiegel_server::{get_closest_color, init};
use tower::ServiceExt;
use tower_http::services::ServeDir;

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    tracing_subscriber::fmt::init();
    init();
    let app = Router::new()
        .route("/color/:rgb_hex", get(fetch_nearest_color))
        .nest_service("/", get(get_static_file));

    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
    Ok(())
}

async fn get_static_file(uri: Uri) -> Result<Response<Body>, (StatusCode, String)> {
    let req = Request::builder().uri(&uri).body(Body::empty()).unwrap();

    match ServeDir::new("assets").oneshot(req).await {
        Ok(res) => Ok(res.map(Body::new)),
        Err(err) => Err((
            StatusCode::INTERNAL_SERVER_ERROR,
            format!("Something went wrong: {}", err),
        )),
    }
}

async fn fetch_nearest_color(
    Path(rgb_hex): Path<String>,
) -> Result<impl IntoResponse, (StatusCode, String)> {
    if rgb_hex.len() != 6 {
        return Err((
            StatusCode::BAD_REQUEST,
            "input should be color hex, eg AA11CC".into(),
        ));
    }
    let closest = get_closest_color(&rgb_hex);

    let headers = [(header::CONTENT_TYPE, "image/jpeg")];
    Ok((headers, closest.image))
}
```
