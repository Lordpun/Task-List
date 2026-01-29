#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(
            tauri_plugin_log::Builder::new()
                .level(log::LevelFilter::Info)
                .build(),
        )
        .plugin(tauri_plugin_shell::init())
        // 3. Initialize the Python plugin
        .plugin(tauri_plugin_python::init_and_register(vec![
            "getTasks",
            "addTask",
            "removeTask",
            "changePriority",
        ]))
        .setup(|_app| {
            Ok(())
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}