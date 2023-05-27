using UnityEngine;

public class PortalSystem : MonoBehaviour
{
    public enum PortalColor
    {
        Orange = 1,
        Blue = 2
    }
    [SerializeField] public PortalColor PortalType;

    [SerializeField] private TeleportationSystem _telSysScr;

    private void OnTriggerStay2D(Collider2D collision)
    {
        if (collision.gameObject.GetComponent<CharacterController>())
        {
            _telSysScr.Teleportation(collision.gameObject, collision.gameObject.GetComponent<Rigidbody2D>());
        }
    }

    // Start is called before the first frame update
    void Start()
    {
        _telSysScr = FindObjectOfType<TeleportationSystem>();
        if(PortalType == PortalColor.Orange)
            _telSysScr.OrangeTeleport = gameObject.transform;
        if (PortalType == PortalColor.Blue)
            _telSysScr.BlueTeleport = gameObject.transform;
    }

    public void DirrectionArrow(float horizontalDirection = 0, float verticalDirection = 0)
    {
        transform.GetChild(0).gameObject.SetActive(true);
        Vector3 groundCheckPos = gameObject.GetComponent<PortalDirection>().groundCheckPos;
        if (horizontalDirection != 0)
            gameObject.transform.GetChild(0).rotation = Quaternion.Euler(new Vector3(0, 0, 90 * horizontalDirection));
        else if (verticalDirection > 0)
            gameObject.transform.GetChild(0).rotation = Quaternion.Euler(new Vector3(0, 0, 180 * verticalDirection));
        else if (verticalDirection < 0)
            gameObject.transform.GetChild(0).rotation = Quaternion.Euler(new Vector3(0, 0, 0));
        gameObject.transform.GetChild(0).position = groundCheckPos - new Vector3(0.5f * horizontalDirection, 0.5f * verticalDirection, 0);
    }
}
