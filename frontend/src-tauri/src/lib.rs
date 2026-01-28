#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
  tauri::Builder::default()
    .setup(|app| {
      if cfg!(debug_assertions) {
        app.handle().plugin(
          tauri_plugin_log::Builder::default()
            .level(log::LevelFilter::Info)
            .build(),
        )?;
      }
      Ok(())
    })

    .plugin(tauri_plugin_python::init_and_register(vec![
      "getTasks",
      "addTask",
      "removeTask",
      "changePriority"
    ]))
    
    .run(tauri::generate_context!())  
    .expect("error while running tauri application");
}
