fn main() {
  tauri_build::build()
}

tauri::Builder::default()
  .plugin(tauri_plugin_python::init())
  .run(tauri::generate_context!())
  .expect("error while running tauri application");