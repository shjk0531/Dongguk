using UnityEngine;

public class InputSystem : MonoBehaviour
{
    [SerializeField] private string InputMove;
    [SerializeField] private KeyCode InputWeaponChange;
    [SerializeField] private KeyCode InputJump;
    [SerializeField] private KeyCode[] InputShootHorizontal;
    [SerializeField] private KeyCode[] InputShootVertical;

    [HideInInspector] public float direction;
    [HideInInspector] public bool isWeaponChange;
    [HideInInspector] public float isJump;
    [HideInInspector] public float shootHorizontal;
    [HideInInspector] public float shootVertical;

    private void Awake()
    {
        DontDestroyOnLoad(this);
    }
    void Update()
    {
        direction = Input.GetAxis(InputMove);

        isWeaponChange = Input.GetKeyDown(InputWeaponChange);

        if (Input.GetKeyDown(InputJump))
            isJump = 1;
        else
            isJump = 0;

        if (Input.GetKeyDown(InputShootHorizontal[0]))
            shootHorizontal = 1;
        else if (Input.GetKeyDown(InputShootHorizontal[1]))
            shootHorizontal = -1;
        else
            shootHorizontal = 0;

        if (Input.GetKeyDown(InputShootVertical[0]))
            shootVertical = 1;
        else if (Input.GetKeyDown(InputShootVertical[1]))
            shootVertical = -1;
        else
            shootVertical = 0;
    }
}
